from django.contrib import admin
from payments.models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'user', 'provider', 'transaction_id', 'amount', 'status', 'created_at')
    search_fields = ('order__id', 'user__username', 'provider', 'transaction_id')
    ordering = ('created_at',)
