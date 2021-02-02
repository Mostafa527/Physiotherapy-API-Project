
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('Clinic', ClinicList.as_view(), name='clinic_list')
]
