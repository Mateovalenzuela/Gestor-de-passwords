from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarPassword/', views.registrarPassword),
    path('edicionPassword/<varId>', views.edicionPassword),
    path('editarPassword/', views.editarPassword),
    path('eliminarPassword/<varId>', views.eliminarPassword),
]