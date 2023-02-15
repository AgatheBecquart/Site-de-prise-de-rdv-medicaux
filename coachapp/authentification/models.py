
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Cette classe représente un utilisateur du système.

    Elle hérite de la classe AbstractUser de Django et ajoute une option de rôle pour distinguer les utilisateurs entre médecins et patients.

    Attributs:
    - role (str): Le rôle de l'utilisateur, qui peut être soit "Médecin" soit "Patient".

    Les valeurs possibles pour le rôle sont définies dans la constante ROLE_CHOICES, qui est un tuple de paires clé-valeur.

    Paramètres:
    - max_length (int): La longueur maximale de la chaîne de caractères représentant le rôle.
    - choices (tuple): Les choix possibles pour le rôle, qui sont définis dans la constante ROLE_CHOICES.
    - verbose_name (str): Le nom à afficher pour le champ "role" dans les formulaires et les pages d'administration.
    - blank (bool): Indique si le champ "role" peut être laissé vide ou non.
    """
    ROLE_CHOICES = (
        ('MEDECIN', 'Médecin'),
        ('PATIENT', 'Patient'),
    )
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle', blank=True)
