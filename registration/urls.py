"""
URL configuration for registration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from core import views as ctv

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('signup/', ctv.signup),
    path('signin/', ctv.signin),
    
    path('successfull/<str:event>/<str:refid>/', ctv.successfull, name='successfull'),
    path('registrationclosed/', ctv.closed, name='failed'),
    
    path('', ctv.home),
    
    
    # Events
    path('webfusionmeet/', ctv.wf),
    path('bitwisebattle/', ctv.bitwisebattle),
    path('designcon/', ctv.designcon),
    path('mechanicalmayhem/', ctv.mechmayhem),
    path('blueprintbash/', ctv.blueprintbash),
    path('sketchup/', ctv.sketchup),
    path('boardbonanza/', ctv.boardbonanza),
    path('challengeshowcase/', ctv.challengeshowcase),
    path('founder\'sfest/', ctv.foundersfest),
]