from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.forms import ContactUsForm
from django.core.mail import send_mail

@login_required
def home(request):
    return render(request, 'blog/home.html')

def contact(request):
    """Cette fonction gère la vue de la page de contact du système.

    Elle utilise le formulaire ContactUsForm pour collecter les informations de l'utilisateur et les envoyer au serveur pour traitement.

    Paramètres :
    - request (HttpRequest) : L'objet de requête HTTP envoyé par le client.

    Retour :
    - HttpResponse : Un objet de réponse HTTP qui affiche la page de contact avec le formulaire ContactUsForm rempli par l'utilisateur si la méthode de requête HTTP est GET, ou traite les données envoyées par l'utilisateur et redirige l'utilisateur vers une page de confirmation si la méthode de requête HTTP est POST.
    """
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

    else:
        form = ContactUsForm()

    return render(request,
                'blog/contact.html',
                {'form': form})
    
def about(request):
    return render(request, 'blog/about.html')

def accueil(request):
    return render(request, 'blog/accueil.html')