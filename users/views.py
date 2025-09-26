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

    Permission classes:
        - Only superusers or unauthenticated users can access this view.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserRegisterSerializer
    permission_classes = [AllowAny, IsSuperUserOrNotAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Creates a new user.

        Returns:
            - 201 Created: If the user is created successfully.
            - 500 Internal Server Error: If an error occurs.
        """
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                if user:
                    logger.info(
                        f"User {user.username} registered successfully."
                    )
                    return Response(serializer.data, status=201)
        except Exception as e:
            logger.error(f"Error occurred while registering user: {str(e)}")
            return Response({"details": str(e)}, status=500)


class UserListView(generics.ListAPIView):
    """
    API view for listing all users.

    Permission classes:
        - Only authenticated users can access this view.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filterset_class = UserFilter
    ordering_fields = ['username']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Returns the queryset for the view.

        If the user is a superuser, returns all users.
        Otherwise, returns only the authenticated user.
        """
        user = self.request.user
        if user.is_superuser:
            return CustomUser.objects.all()
        return CustomUser.objects.filter(id=user.id)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a user.

    Permission classes:
        - Allows only the authenticated user or superusers to access this view.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, IsAdminOrSelf]
