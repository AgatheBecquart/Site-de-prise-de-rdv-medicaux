# Generated by Django 4.1.6 on 2023-02-14 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_alter_appointment_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.CharField(choices=[('2023-02-14', '14 févr. 2023'), ('2023-02-15', '15 févr. 2023'), ('2023-02-16', '16 févr. 2023'), ('2023-02-17', '17 févr. 2023'), ('2023-02-18', '18 févr. 2023'), ('2023-02-19', '19 févr. 2023'), ('2023-02-20', '20 févr. 2023'), ('2023-02-21', '21 févr. 2023'), ('2023-02-22', '22 févr. 2023'), ('2023-02-23', '23 févr. 2023')], default='Lundi 20 Février', max_length=30),
        ),
    ]
