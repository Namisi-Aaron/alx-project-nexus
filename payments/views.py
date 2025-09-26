from rest_framework import generics, permissions
from payments.models import Payment
from payments.serializers import PaymentSerializer


class PaymentListCreateView(generics.ListCreateAPIView):
    """
    API view for listing all payments and creating payments for a specific user.

    Permission classes:
        - Only authenticated users can access this view.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PaymentSerializer
    ordering_fields = ['user', 'status']
    queryset = Payment.objects.all()

    def get_queryset(self):
        """
        Returns all payments for the authenticated user.
        """
        user = self.request.user
        if user.is_superuser:
            return Payment.objects.all()
        return Payment.objects.filter(user=self.request.user)


class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific payment.

    Permission classes:
        - Admins or the owner of the payment can access this view.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def get_queryset(self):
        """
        Returns all payments for the authenticated user.
        """
        user = self.request.user
        if user.is_superuser:
            return Payment.objects.all()
        return Payment.objects.filter(user=self.request.user)
