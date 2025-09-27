from django.contrib import admin
from users.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'phone_number')
    search_fields = ('username', 'role', 'phone_number',)
    ordering = ('-date_joined',)
