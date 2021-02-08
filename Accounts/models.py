
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

USER_TYPE_CHOICES = (
    ('admin', 'admin'),
    ('doctor', 'doctor'),
    ('patient', 'patient'),
    ('staff', 'staff'),
    ('user_admin', 'user_admin'),
)
class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, first_name, password, **other_fields)
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
    user_type = models.CharField(max_length=40, choices=USER_TYPE_CHOICES ,default=USER_TYPE_CHOICES[3][1],blank=True,null=True)


    def __str__(self):
        return self.username

