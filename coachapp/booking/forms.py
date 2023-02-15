from django import forms
from .models import Appointment, Note

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['client', 'date', 'heure', 'objet']

class NoteForm(forms.ModelForm):
    text = forms.CharField(label="Ajouter une note")

    class Meta:
        model = Note
        fields = ['text']
