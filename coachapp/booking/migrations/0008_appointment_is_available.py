# Generated by Django 4.1.6 on 2023-02-13 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_alter_appointment_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]