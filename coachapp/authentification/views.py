from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.conf import settings
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

def logout_user(request):
    """Cette fonction permet à l'utilisateur actuellement connecté de se déconnecter du système.

    Elle appelle la méthode logout() de Django pour vider la session de l'utilisateur en cours, puis redirige l'utilisateur vers la page de connexion.

    Paramètres:
    - request (HttpRequest): L'objet de requête HTTP envoyé par le client.

    Retour:
    - HttpResponseRedirect : Un objet de réponse HTTP qui redirige l'utilisateur vers la page de connexion.
    """
    logout(request)
    return redirect('login')

class LoginPageView(LoginRequiredMixin, View):
    """Cette classe gère la vue de la page de connexion du système.

    Elle hérite de la classe LoginRequiredMixin de Django, qui vérifie si l'utilisateur est connecté avant de lui donner accès à la vue. Elle utilise un formulaire LoginForm pour collecter les informations d'identification de l'utilisateur et les envoyer au serveur.

    Attributs:
    - template_name (str): Le nom du fichier de modèle HTML qui sera utilisé pour afficher la page de connexion.
    - form_class (LoginForm): La classe de formulaire utilisée pour collecter les informations d'identification de l'utilisateur.

    Méthodes:
    - get(self, request): Cette méthode est appelée lorsque l'utilisateur accède à la page de connexion. Elle renvoie le formulaire LoginForm vide et un message vide à afficher.
    - post(self, request): Cette méthode est appelée lorsque l'utilisateur soumet le formulaire LoginForm. Elle vérifie si les informations d'identification de l'utilisateur sont valides, authentifie l'utilisateur et le redirige vers la page d'accueil s'il est authentifié avec succès. Sinon, elle affiche un message d'erreur et renvoie le formulaire LoginForm rempli avec les informations fournies par l'utilisateur.

    Paramètres:
    - request (HttpRequest): L'objet de requête HTTP envoyé par le client.

    Retour:
    - HttpResponse : Un objet de réponse HTTP qui affiche la page de connexion avec le formulaire LoginForm et éventuellement un message d'erreur si l'authentification échoue.
    """
    template_name = 'authentication/login.html'
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})
        
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Identifiants invalides.'
        return render(request, self.template_name, context={'form': form, 'message': message})
    


def signup_page(request):
    """Cette fonction gère la vue de la page d'inscription du système.

    Elle utilise un formulaire SignupForm pour collecter les informations de l'utilisateur et les envoyer au serveur pour créer un nouveau compte d'utilisateur.

    Paramètres :
    - request (HttpRequest) : L'objet de requête HTTP envoyé par le client.

    Retour :
    - HttpResponse : Un objet de réponse HTTP qui affiche la page d'inscription avec le formulaire SignupForm rempli par l'utilisateur si le formulaire n'est pas valide, ou redirige l'utilisateur vers la page de connexion s'il est inscrit avec succès.
    """
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentification/signup.html', context={'form': form})

