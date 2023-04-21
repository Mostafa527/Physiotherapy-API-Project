from django.urls import path
from . import views
from .views import *
#URLS Pattern Comment
urlpatterns = [
#Paths
path('Scores/<int:session_id>',views.ScoresBySessionID,name='ScoresBySessionID'),
path('Score',ScoreList.as_view(),name='score_list'),
]