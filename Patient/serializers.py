from Accounts.serializers import UserSerializer
from .models import Patient
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('pk','user', 'Physio_Patient',)
        read_only_fields = ('pk',)


class PatientProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Patient
        fields = ('user', 'Physio_Patient',)
        read_only_fields = ('id','is_patient',)


