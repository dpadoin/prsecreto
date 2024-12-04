"""
URL configuration for psecreto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from . import views
from .views import formulario, sucesso, entrada, teste, visualizar_tabela, salvar_desc, visualizar_tabela2

urlpatterns = [
    path("admin/", admin.site.urls),
    path('/', entrada, name='entrada'),
    path('entrada/', entrada, name='entrada'),
    path('formulario/', formulario, name='formulario'),
    path('sucesso/', sucesso, name='sucesso'),
    path('teste/', teste, name='teste'),
    path('visualizar-tabela/', visualizar_tabela, name='visualizar_tabela'),
    path('visualizar-tabela2/', visualizar_tabela2, name='visualizar_tabela2'),
    path('salvar_desc/', salvar_desc, name='salvar_desc'),
]
