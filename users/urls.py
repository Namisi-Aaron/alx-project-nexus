from django.urls import path


from users.views import UserListView, UserDetailView, UserCreateView
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'users', UserViewset, basename='users')
# urlpatterns = router.urls

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
