
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
class ClinicList(APIView):
    def get(self,request):
        clinics = Clinic.objects.all()
        data=ClinicSerializer(clinics,many=True).data
        return Response(data)



