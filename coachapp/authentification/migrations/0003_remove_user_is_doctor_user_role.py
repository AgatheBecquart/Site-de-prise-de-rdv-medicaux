# Generated by Django 4.1.6 on 2023-02-12 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0002_remove_user_role_user_is_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_doctor',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('MEDECIN', 'Médecin'), ('PATIENT', 'Patient')], max_length=30, verbose_name='Rôle'),
        ),
    ]
