
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
   path('admin/', admin.site.urls),
    path('', include('Clinic.urls')),
    path('', include('Accounts.urls')),
    path('', include('MyAdmin.urls'))
]
