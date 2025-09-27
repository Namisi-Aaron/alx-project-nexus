import django_filters
from users.models import CustomUser


class UserFilter(django_filters.FilterSet):
    """
    Filter for CustomUser model.

    Fields:
        username: Filter by username.
        email: Filter by email.
        phone_number: Filter by phone number.
        role: Filter by user role.
    """
    username = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    phone_number = django_filters.CharFilter(lookup_expr='icontains')
    role = django_filters.ChoiceFilter(choices=CustomUser.USER_ROLES)

    class Meta:
        """
        Meta options for UserFilter.
        """
        model = CustomUser
        fields = ['username', 'role', 'email', 'phone_number']
        ordering_fields = ['username']
