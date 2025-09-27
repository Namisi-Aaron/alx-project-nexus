from django.contrib import admin
from orders.models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'shipping_address', 'total_amount', 'created_at')
    search_fields = ('id', 'user__username', 'status', 'shipping_address')
    ordering = ('-id',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price','subtotal')
    search_fields = ('id', 'order__id', 'product__name')
    ordering = ('id',)
