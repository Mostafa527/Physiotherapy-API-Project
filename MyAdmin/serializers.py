from Accounts.serializers import UserSerializer
from .models import MyAdmin
from rest_framework import serializers

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyAdmin
        fields = ('pk','user', 'Admin_Clinic',)
        read_only_fields = ('pk',)


class AdminProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = MyAdmin
        fields = ('user', 'Admin_Clinic',)
        read_only_fields = ('is_admin','id',)
