# Generated by Django 4.1.6 on 2023-02-14 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_alter_appointment_date_alter_appointment_heure'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='Client',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
