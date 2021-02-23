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

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data.is_admin = True
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user.is_admin = True
        user.user_type = 'admin'
        user.save()
        myadmin, created = MyAdmin.objects.update_or_create(user=user,
                                                            Admin_Clinic=validated_data.pop('Admin_Clinic'))
        return myadmin