# Generated by Django 4.2.3 on 2023-07-27 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, unique=True)),
                ('Address', models.CharField(max_length=300)),
                ('Contact', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=150, unique=True)),
            ],
        ),
    ]
