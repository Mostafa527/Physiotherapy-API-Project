
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True,null=True)
    last_name = models.CharField(max_length=150, blank=True,null=True)
    password2 = models.CharField(max_length=120)
    Address = models.CharField(max_length=300)
    Contact = models.CharField(max_length=25)
    BirthDate =models.DateField(auto_now=False, blank=True, null=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)

    def __str__(self):
        return self.username

