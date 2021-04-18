
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
   path('admin/', admin.site.urls),
    path('', include('Clinic.urls')),
    path('', include('Accounts.urls')),
    path('', include('MyAdmin.urls')),
    path('', include('Physiotherapist.urls')),
    path('', include('Patient.urls')),
    path('',include('Game.urls')),
    path('',include('Session.urls')),
    path('',include('Scores.urls'))
]
