
from django.urls import path
from .views import *
urlpatterns = [
    path('Clinic', ClinicList.as_view(), name='clinic_list')
]
