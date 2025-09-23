import logging
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.permissions import IsSuperUserOrNotAuthenticated, IsAdminOrSelf
from users.models import CustomUser
from users.filters import UserFilter
from users.serializers import (
    CustomUserSerializer,
    CustomUserRegisterSerializer
)

logger = logging.getLogger(__name__)
    
class UserCreateView(generics.CreateAPIView):
    """
    API view for creating a new user.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserRegisterSerializer
    permission_classes = [AllowAny, IsSuperUserOrNotAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                if user:
                    logger.info(f"User {user.username} registered successfully.")
                    return Response(serializer.data, status=201)
        except Exception as e:
            logger.error(f"Error occurred while registering user: {str(e)}")
            return Response({"details": str(e)}, status=500)

class UserListView(generics.ListAPIView):
    """
    API view for listing all users.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filterset_class = UserFilter
    ordering_fields = ['username']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return CustomUser.objects.all()
        return CustomUser.objects.filter(id=user.id)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, IsAdminOrSelf]
