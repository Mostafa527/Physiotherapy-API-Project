
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from django.http import Http404

class physio_detail(APIView):
    def get_object(self, pk):
        try:
            return Physiotherapist.objects.get(pk=pk)
        except Physiotherapist.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        physio = self.get_object(pk)
        serializer = PhysioProfileSerializer(physio)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        physio = self.get_object(pk)

        serializer = PhysioProfileSerializer(physio, data=request.data)
        if serializer.is_valid():
            
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)