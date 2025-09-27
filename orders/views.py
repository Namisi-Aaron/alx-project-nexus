from django.shortcuts import get_object_or_404
from orders.models import Order, OrderItem
from orders.tasks import send_order_creation_email
from products.models import Product
from orders.serializers import OrderSerializer, OrderItemSerializer
from rest_framework import generics, permissions


class OrderListCreateView(generics.ListCreateAPIView):
    """
    API view for listing all orders and creating orders for a specific user.

    Permission classes:
        - Only authenticated users can access this view.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    ordering_fields = ['user', 'status']
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Returns all orders for the authenticated user.
        """
        user = self.request.user
        if user.is_superuser:
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        """
        Create the user and send a notification email to the user.
        """
        order = serializer.save(user=self.request.user)
        send_order_creation_email.delay(order.id, order.user.email, order.user.username)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific order.

    Permission classes:
        - Admins or the owner of the order can access this view.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)


class OrderItemListCreateView(generics.ListCreateAPIView):
    """
    API view for listing and creating order items for a specific order.
    """
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Return all order items for this order.
        - Admins see all items.
        - Normal users see only their own order items.
        """
        order_id = self.kwargs.get("order_id")
        user = self.request.user

        if user.is_superuser:
            return OrderItem.objects.filter(order_id=order_id)

        return OrderItem.objects.filter(order__user=user, order_id=order_id)

    def perform_create(self, serializer):
        """
        Create a new order item for the specified order.
        Ensures that the order belongs to the current user (unless admin).
        """
        order = get_object_or_404(
            Order.objects.filter(user=self.request.user)
            if not self.request.user.is_superuser else Order.objects.all(),
            id=self.kwargs["order_id"]
        )

        product = get_object_or_404(Product, id=self.request.data.get("product"))

        serializer.save(
            order=order,
            product=product,
            price=product.price
        )


class OrderItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific order item.
    """
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Restrict the queryset based on the order and user.
        - Admins see all order items for the given order.
        - Normal users see only their own order items.
        """
        order_id = self.kwargs.get("order_id")
        user = self.request.user

        if user.is_superuser:
            return OrderItem.objects.filter(order_id=order_id)

        return OrderItem.objects.filter(order__user=user, order_id=order_id)
