
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import Http404

class patient_detail(APIView):
    def get_object(self, pk):
        try:
            return Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        patient = self.get_object(pk)
        print(patient.pk)
        serializer = PatientProfileSerializer(patient)
        return Response(serializer.data)