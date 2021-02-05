from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
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



