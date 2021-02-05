from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from django.http import Http404

class clinic_detail(APIView):
    def get_object(self, pk):
        try:
            return Clinic.objects.get(pk=pk)
        except Clinic.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        clinic = self.get_object(pk)
        serializer = ClinicSerializer(clinic)
        return Response(serializer.data)

class ClinicList(APIView):
    def get(self,request):
        clinics = Clinic.objects.all()
        data=ClinicSerializer(clinics,many=True).data
        return Response(data)

    def post(self, request):
        serializer = ClinicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



