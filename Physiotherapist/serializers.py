from Accounts.serializers import UserSerializer
from .models import Physiotherapist
from rest_framework import serializers

class PhysioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Physiotherapist
        fields = ('pk','user', 'Clinic_Physio',)
        read_only_fields = ('pk',)


class PhysioProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Physiotherapist
        fields = ('user', 'Clinic_Physio',)
        read_only_fields = ('id','is_doctor',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user.is_doctor = True
        user.user_type = 'doctor'
        user.save()
        physio, created = Physiotherapist.objects.update_or_create(user=user,
                                                                   Clinic_Physio=validated_data.pop('Clinic_Physio'))
        return physio
