from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from client.models import Client, User


class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'role',
            'password']

        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            password=validated_data["password"],
        )

    def validate_password(self, value: str) -> str:
        return make_password(value)


class UserSerializer(ModelSerializer): 
                
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
            'role', 'password']

    def validate_password(self, value: str) -> str:
            return make_password(value)


class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'email', 'company_name',
            'sales_contact']

    def validate_password(self, value: str) -> str:
        return make_password(value)


"""
first_name, last_name, email, phone, mobile, company_name, sales_contact, role
"""