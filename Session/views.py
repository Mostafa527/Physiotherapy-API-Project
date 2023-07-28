
from rest_framework import status
from rest_framework.response import Response
from ExercisePlan.models import Exercise_Plan
from .models import Session
from .serializers import SessionSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
@api_view(['GET'])
def SessionByExercisePlan(request,exerciseplan_id):
    try:
        exercise_plan = Exercise_Plan.objects.get(p_k=exerciseplan_id)
    except Exercise_Plan.DoesNotExist:
        return Response({'message': 'The ExercisePlan does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            session=exercise_plan.session_plan.all()
        except Session.DoesNotExist:
            return Response({'message': 'The Session does not exist'}, status=status.HTTP_404_NOT_FOUND)
        session_serializer =SessionSerializer(session,many=True)
        return Response(session_serializer.data)