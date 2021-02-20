from django.db import models
from Clinic.models import Clinic
from Accounts.models import NewUser
class MyAdmin(models.Model):
    user = models.OneToOneField(NewUser, on_delete=models.CASCADE, primary_key=True, related_name='admin_user')

    Admin_Clinic =models.ForeignKey(Clinic,related_name='admins',on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
