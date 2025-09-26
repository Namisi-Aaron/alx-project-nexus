import uuid
import requests
from rest_framework import generics, permissions, views
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from payments.models import Payment
from payments.serializers import PaymentSerializer
from payments.utils import initialize_chapa_payment


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
        return Payment.objects.filter(user=user)
    
    def perform_create(self, serializer):
        """
        Sets the user for the created payment to the authenticated user.
        """
        order = serializer.validated_data.get("order")
        if order is None:
            raise PermissionDenied("Order is required.")

        if not self.request.user.is_superuser and order.user != self.request.user:
            raise PermissionDenied("You cannot create a payment for someone else's order.")
        
        tx_ref = f"order-{order.id}-{uuid.uuid4().hex[:8]}"

        chapa_response = initialize_chapa_payment(
            amount=order.total_amount,
            email=order.user.email,
            first_name=order.user.first_name,
            last_name=order.user.last_name,
            phone_number=order.user.phone_number,
            tx_ref=tx_ref,
        )

        if chapa_response.get("status") != "success":
            raise PermissionDenied(f"Payment initialization failed: {chapa_response}")
        
        checkout_url = chapa_response.get("data", {}).get("checkout_url")

        payment = serializer.save(
            user=order.user,
            transaction_id=tx_ref,
        )

        self.checkout_url = checkout_url
        self.payment_id = payment.id

    def create(self, request, *args, **kwargs):
        response_obj = super().create(request, *args, **kwargs)
        response_obj.data["checkout_url"] = getattr(self, "checkout_url", None)
        response_obj.data["payment.id"] = getattr(self, "payment.id", None)
        return response_obj


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


class ChapaWebhookView(views.APIView):
    """
    API view for handling Chapa's webhook.
    """
    permission_classes = []
    authentication_classes = []

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        tx_ref = data.get("tx_ref")

        if not tx_ref:
            return response.Response({"status": "tx_ref missing"}, status=400)
        
        try:
            payment = Payment.objects.get(transaction_id=tx_ref)
        except Payment.DoesNotExist:
            return response.Response({"status": "Payment not found"}, status=404)
        
        verify_url = f"https://api.chapa.co/v1/transaction/verify/{tx_ref}"
        headers = {"Authorization": f"Bearer CHASECK_TEST-Dfgb6aAXMA5KrIcrwwH1sy4qUJhrAUtM"}
        response = requests.get(verify_url, headers=headers)

        verify_data = response.json()

        if verify_data.get("status") == "success" and verify_data.get("data", {}).get("status") == "success":
            payment.status = "completed"
            payment.save()
            return Response({"status": "Payment verified and updated."}, status=200)
        
        payment.status = "failed"
        payment.save()
        return Response({"status": "Payment failed."}, status=400)