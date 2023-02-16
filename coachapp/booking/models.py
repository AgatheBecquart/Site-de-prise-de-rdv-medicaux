from django.db import models
from django.contrib.auth import get_user_model
import datetime
from babel.dates import format_date
from django.utils import timezone
from django.core.exceptions import ValidationError
import pandas as pd
import locale

User = get_user_model()
        

class Appointment(models.Model):
    """La classe Appointment représente un modèle de rendez-vous.
    La classe a également les méthodes suivantes :

    clean: méthode qui vérifie que l'horaire du rendez-vous n'est pas déjà pris par un autre rendez-vous pour la même date et lève une exception ValidationError si c'est le cas
    is_past_due: une propriété booléenne qui renvoie True si le rendez-vous est passé, sinon False
    get_date_display: méthode qui renvoie une chaîne de caractères qui représente la date de rendez-vous au format "jour_semaine jour_mois année" en utilisant la langue française.
    """
    
    TIME_CHOICES = (
    ("09:00 - 09:20", "9h - 9h20"),
    ("09:30 - 09:50", "9h30 - 9h50"),
    ("10:00 - 10:20", "10h - 10h20"),
    ("10:30 - 10:50", "10h30 - 10h50"),
    ("11:00 - 11:20", "11h - 11h20"),
    ("11:30 - 11:50", "11h30 - 11h50"),
    ("12:00 - 12:20", "12h - 12h20"),
    ("12:30 - 12:50", "12h30 - 12h50"),
    ("13:30 - 13:50", "13h30 - 13h50"),
    ("14:00 - 14:20", "14h - 14h20"),
    ("14:30 - 14:50", "14h30 - 14h50"),
    ("15:00 - 15:20", "15h - 15h20"),
    ("15:30 - 15:50", "15h30 - 15h50"),
    ("16:00 - 16:20", "16h - 16h20"),
    ("16:30 - 16:50", "16h30 - 16h50"),
)

    today = pd.Timestamp.now().floor('D') + pd.Timedelta(days=1)  # commencer à partir du lendemain
    DAY_CHOICES = []
    for i in range(12):
        day = today + pd.Timedelta(days=i)
        if day.dayofweek < 5:  # 0 = Lundi, 4 = Vendredi
            formatted_date = format_date(day.to_pydatetime(), format='full', locale='fr_FR')
            DAY_CHOICES.append((day.strftime("%Y-%m-%d"), formatted_date))
        
    client = models.CharField(max_length=20,null=True, blank=True)   
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.CharField(max_length=30, choices=DAY_CHOICES, default=DAY_CHOICES[0][0])
    heure = models.CharField(max_length=50, choices=TIME_CHOICES, default=TIME_CHOICES[0][0])
    objet = models.CharField(max_length=255,null=True, blank=True)
    time_ordered = models.DateTimeField(default=timezone.now, blank=True)
    
    def clean(self):
        appointments = Appointment.objects.filter(date=self.date, heure=self.heure)
        if appointments.exists():
            raise ValidationError("Cet horaire est déjà pris.")
        
    @property
    def is_past_due(self):
        date_rdv=self.date.split("-")
        heure_rdv=self.heure[0:2]
        date_rdv=datetime.datetime(int(date_rdv[0]),int(date_rdv[1]),(int(date_rdv[2])),(int(heure_rdv)))
        return datetime.datetime.today() > date_rdv
    
    def get_date_display(self):
        locale.setlocale(locale.LC_TIME, 'fr_FR.utf8')
        return datetime.datetime.strptime(self.date, '%Y-%m-%d').strftime('%A %d %B %Y')
    


class Note(models.Model):
    """Modèle représentant une note écrite par un utilisateur.

    Attributs:
    - user: ForeignKey vers un objet User représentant l'utilisateur lié au rendez-vous pour lequel on consultera l'historique.
    - text: texte de la note. Chaîne de caractères pouvant contenir jusqu'à 255 caractères. 
    - created_date: date de création de la note. Date et heure stockées sous forme d'un objet DateTime. Par défaut, la date et l'heure actuelles sont enregistrées.

    Méthodes:
    - __str__ : Retourne une représentation sous forme de chaîne de caractères de la note, correspondant à son texte.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.CharField(max_length=255,null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text