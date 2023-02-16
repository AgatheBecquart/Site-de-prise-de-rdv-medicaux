from django.shortcuts import render, redirect, get_object_or_404
from .forms import AppointmentForm, NoteForm
from django.contrib.auth.decorators import login_required
from .models import Appointment, Note

@login_required
def create_appointment(request):
    """
    Permet à un utilisateur connecté de créer un nouveau rendez-vous. Si la méthode de la requête est POST, vérifie la validité des données du formulaire de rendez-vous. Si le formulaire est valide, crée un nouvel objet Appointment avec les données du formulaire et les informations de l'utilisateur connecté, puis redirige vers la page de consultation des rendez-vous. Si le formulaire n'est pas valide, l'affiche à nouveau. Si la méthode de la requête est GET, affiche un formulaire vide de rendez-vous. Si l'utilisateur connecté n'est pas un médecin, supprime le champ "client" du formulaire. 
        
    Retour:
        - Un objet HttpResponse avec le modèle de rendu pour la page de création de rendez-vous, contenant le formulaire de rendez-vous. Si le formulaire n'est pas valide, affiche également les erreurs de validation du formulaire.
    """
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.full_clean()
            appointment.save()
            return redirect('consult')
    else:
        form = AppointmentForm()
        if request.user.role != 'MEDECIN':
            del form.fields['client']
    return render(request, 'booking/create_appointment.html', {'form': form})


def consult_appointment(request):
    """
    Vue qui gère l'affichage des rendez-vous d'un client connecté.

    Cette vue affiche les rendez-vous de l'utilisateur connecté en filtrant les rendez-vous stockés en base de données avec le champ 'user' égal à l'utilisateur connecté.

    Args:
        request: objet HttpRequest représentant la requête HTTP reçue.

    Returns:
        HttpResponse représentant la page HTML affichant la liste des rendez-vous de l'utilisateur connecté.
        Les rendez-vous sont passés à la page via le dictionnaire de contexte 'appointments'.
    """
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'booking/consult_appointment.html', {'appointments': appointments})


@login_required
def manage_appointment(request):
    """
    Vue qui gère l'affichage des rendez-vous pour le médecin.

    Args:
        request: objet HttpRequest représentant la requête HTTP reçue.

    Returns:
        HttpResponse représentant la page HTML affichant la liste de tous les rendez-vous pris par les clients.
        Les rendez-vous sont passés à la page via le dictionnaire de contexte 'appointments'.
    """
    appointments = Appointment.objects.all()
    return render(request, 'booking/manage_appointment.html', {'appointments': appointments})

@login_required
def appointment_change(request, id):
    """
    Vue qui gère la modification d'un rendez-vous.

    Args:
        request: objet HttpRequest représentant la requête HTTP reçue.
        id: identifiant unique du rendez-vous à modifier.

    Returns:
        HttpResponse représentant la page HTML pour la modification d'un rendez-vous.
        Si le formulaire est valide et a été enregistré avec succès, l'utilisateur sera redirigé soit vers la page de gestion de rendez-vous (pour les médecins), soit vers la page de consultation de rendez-vous (pour les patients).
        Si le formulaire n'est pas valide, l'utilisateur verra le formulaire de modification de rendez-vous avec les erreurs correspondantes.

    Raises:
        Appointment.DoesNotExist: si le rendez-vous avec l'identifiant spécifié n'existe pas en base de données.
    """
    appointment = Appointment.objects.get(id=id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            if request.user.role == 'MEDECIN':
                    return redirect('manage') 
            else:
                return redirect('consult') 
        elif not form.is_valid():
            form = AppointmentForm(instance=appointment)
            del form.fields['client']
    else:
        form = AppointmentForm(instance=appointment)
        del form.fields['client']
    return render(request,
                    'booking/appointment_change.html',
                    {'form': form})
 
@login_required   
def appointment_delete(request, id):
    """Supprime un rendez-vous existant.

    Args:
        id (int): l'identifiant unique du rendez-vous à supprimer.

    Returns:
        HttpResponse : une réponse HTTP redirigeant l'utilisateur en fonction de son rôle.

        Si la requête est une méthode POST et que le rendez-vous a été supprimé avec succès, les utilisateurs avec le rôle "MEDECIN" sont redirigés vers la page de gestion de rendez-vous ('manage'), tandis que les autres utilisateurs sont redirigés vers la page de consultation de rendez-vous ('consult').

    Raises:
        Appointment.DoesNotExist : si aucun rendez-vous correspondant à l'identifiant fourni n'a été trouvé.
    """
   
    appointment = Appointment.objects.get(id=id)

    if request.method == 'POST':
        appointment.delete()
        if request.user.role == 'MEDECIN':
                    return redirect('manage') 
        else:
            return redirect('consult') 
    return render(request,
                    'booking/appointment_delete.html',
                    {'appointment': appointment})
    
@login_required   
def appointment_detail(request, id):
    """
    Vue qui gère l'affichage des notes qui sont associées au client qui a pris le rendez-vous.

    Args:
        request: objet HttpRequest représentant la requête HTTP reçue.
        id: identifiant unique du rendez-vous à afficher.

    Returns:
        HttpResponse représentant la page HTML pour l'affichage de l'historique du client du rendez-vous et des notes qui lui sont associées.
        Les informations du rendez-vous, les notes associées, ainsi que le formulaire de création de notes sont passés à la page via le dictionnaire de contexte.

    Raises:
        Appointment.DoesNotExist: si le rendez-vous avec l'identifiant spécifié n'existe pas en base de données.
    """
    appointment = get_object_or_404(Appointment, id=id)
    user = appointment.user
    notes = Note.objects.filter(user=user)

    if request.method == 'POST':
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            note = note_form.save(commit=False)
            note.user = user
            note.appointment = appointment
            note.save()
            return redirect('manage')
    else:
        note_form = NoteForm()

    return render(request, 'booking/appointment_detail.html', {'user': user, 'notes': notes, 'note_form': note_form})