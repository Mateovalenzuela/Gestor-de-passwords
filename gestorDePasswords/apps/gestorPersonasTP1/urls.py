from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarPersona/', views.registrarPersona),
    path('edicionPersona/<varId>', views.edicionPersona),
    path('editarPersona/', views.editarPersona),
    path('eliminarPersona/<varId>', views.eliminarPersona),
]