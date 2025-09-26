from django.urls import path
from orders.views import (
    OrderListCreateView, OrderDetailView,
    OrderItemListCreateView, OrderItemDetailView
)

urlpatterns = [
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path(
        'orders/<int:order_id>/items/',
        OrderItemListCreateView.as_view(), name='order-item-list-create'
    ),
    path(
        'orders/<int:order_id>/items/<int:pk>/',
        OrderItemDetailView.as_view(), name='order-item-detail'
    ),
]
