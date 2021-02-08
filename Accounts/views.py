
from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.http import Http404
from .serializers import UserSerializer

from rest_framework.response import Response


class RegisterView(APIView):
    def get(self, request):
        admins = NewUser.objects.all()
        data = UserSerializer(admins, many=True).data
        return Response(data)



class user_detail(APIView):

    def get_object(self, pk):
        try:
            return NewUser.objects.get(pk=pk)
        except NewUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserSerializer(snippet)
        print(snippet.pk)
        return Response(serializer.data)


