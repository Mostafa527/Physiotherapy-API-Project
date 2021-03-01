# Generated by Django 4.2.3 on 2023-07-27 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clinic', '0001_initial'),
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Physiotherapist',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='physio_user', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Clinic_Physio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pysio_therpists', to='Clinic.clinic')),
            ],
        ),
    ]
