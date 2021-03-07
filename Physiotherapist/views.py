
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

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
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        physio = self.get_object(pk)
        physio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PhysioList(APIView):
    def get(self,request):
        physio = Physiotherapist.objects.all()
        data=PhysioProfileSerializer(physio,many=True).data
        return Response(data)
    def post(self,request):
        serializer = PhysioProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)