
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.http import Http404

class admin_detail(APIView):
    def get_object(self, pk):
        try:
            return MyAdmin.objects.get(pk=pk)
        except MyAdmin.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        print(snippet.pk)
        serializer = AdminProfileSerializer(snippet)
        return Response(serializer.data)