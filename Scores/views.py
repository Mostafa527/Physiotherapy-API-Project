
from rest_framework import status
from rest_framework.response import Response
from Session.models import Session
from .models import Scores
from .serializers import ScoreSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

#get ScoresUsingSessionID
@api_view(['GET'])
def ScoresBySessionID(request,session_id):
    try:
        session = Session.objects.get(pk=session_id)
    except Session.DoesNotExist:
        return Response({'message': 'The Session does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            scores=session.session_score.all()
        except Scores.DoesNotExist:
            return Response({'message': 'No Scores'}, status=status.HTTP_404_NOT_FOUND)
        score_serializer =ScoreSerializer(scores,many=True)
        return Response(score_serializer.data)