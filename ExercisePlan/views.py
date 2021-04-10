from rest_framework import status
from rest_framework.response import Response
from Patient.serializers import PatientProfileSerializer
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import Http404
from .models import  Exercise_Plan
class exerciseplan_detail(APIView):
    def get_object(self, pk):
        try:
            return Exercise_Plan.objects.get(pk=pk)
        except Exercise_Plan.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        exercise_plan = self.get_object(pk)
        serializer = Exercise_Plan_Serializer(exercise_plan)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        exercise_plan = self.get_object(pk)

        serializer = Exercise_Plan_Serializer(exercise_plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete_(self, request, pk, format=None):
        exercise_plan = self.get_object(pk)
        exercise_plan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
