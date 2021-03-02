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

