
from django.conf import settings
from Accounts.models import NewUser
from rest_framework.exceptions import ValidationError
from physiotherpy import settings
from rest_framework import exceptions
from django.contrib import auth
from rest_framework import serializers
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}
    )
    class Meta:
        model = NewUser
        fields = ('id', 'username','first_name','last_name', 'password', 'password2', 'email','Contact', 'Address', 'is_admin','is_doctor','is_patient', 'user_type')
        read_only_fields = ('id', 'is_admin','is_patient','is_doctor','user_type')
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.pop('password2')
        if password != confirm_password:
            raise ValidationError("Passwords doesn't match.")
        return data
