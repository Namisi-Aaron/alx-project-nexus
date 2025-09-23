from users.models import CustomUser
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    """ Serializer for CustomUser model """
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'phone_number']
        read_only_fields = ['id', 'role']


class CustomUserRegisterSerializer(serializers.ModelSerializer):
    """ Serializer for registering a new user """
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'phone_number']

    def create(self, validated_data):
        """
        Creates a new user with the validated data.
        """
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
