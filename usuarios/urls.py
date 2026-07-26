from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_usuarios, name='lista_usuarios'),
]