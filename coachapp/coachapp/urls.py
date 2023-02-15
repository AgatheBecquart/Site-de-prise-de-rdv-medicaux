"""coachapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import authentification.views, blog.views, booking.views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.accueil, name='accueil'),
    path('login/', LoginView.as_view(
            template_name='authentification/login.html',
            redirect_authenticated_user=True),
        name='login'),
    path('logout/', authentification.views.logout_user, name='logout'),
    path('home/', blog.views.home, name='home'),
    path('signup/', authentification.views.signup_page, name='signup'),
    path('booking/', booking.views.create_appointment, name='booking'),
    path('consult/', booking.views.consult_appointment, name='consult'),
    path('manage/', booking.views.manage_appointment, name='manage'),
    path('contact-us/',blog.views.contact, name='contact'),
    path('about-us/', blog.views.about, name='about'),
    path('booking/', booking.views.create_appointment, name='booking'),
    path('<int:id>/change/', booking.views.appointment_change, name='appointment-change'),
    path('<int:id>/delete/', booking.views.appointment_delete, name='appointment-delete'),
    path('<int:id>/details/', booking.views.appointment_detail, name='appointment-detail'),
]