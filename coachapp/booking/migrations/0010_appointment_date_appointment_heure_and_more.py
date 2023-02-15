# Generated by Django 4.1.6 on 2023-02-13 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_rename_heure_appointment_horaire_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.CharField(choices=[('2023-02-13', '13 févr. 2023'), ('2023-02-14', '14 févr. 2023'), ('2023-02-15', '15 févr. 2023'), ('2023-02-16', '16 févr. 2023'), ('2023-02-17', '17 févr. 2023'), ('2023-02-18', '18 févr. 2023'), ('2023-02-19', '19 févr. 2023'), ('2023-02-20', '20 févr. 2023'), ('2023-02-21', '21 févr. 2023'), ('2023-02-22', '22 févr. 2023')], default='Lundi 20 Février', max_length=30),
        ),
        migrations.AddField(
            model_name='appointment',
            name='heure',
            field=models.CharField(choices=[('9 AM', '9 AM'), ('9:30 AM', '9:30 AM'), ('10 AM', '10 AM'), ('10:30 AM', '10:30 AM'), ('11 AM', '11 AM'), ('11:30 AM', '11:30 AM'), ('12 PM', '12 PM'), ('12:30 PM', '12:30 PM'), ('1:30 PM', '1:30 PM'), ('2 PM', '2 PM'), ('2:30 PM', '2:30 PM'), ('3 PM', '3 PM'), ('3:30 PM', '3:30 PM'), ('4 PM', '4 PM'), ('4:30 PM', '4:30 PM'), ('5 PM', '5 PM')], default='3 PM', max_length=10),
        ),
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together={('date', 'heure')},
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='horaire',
        ),
    ]
