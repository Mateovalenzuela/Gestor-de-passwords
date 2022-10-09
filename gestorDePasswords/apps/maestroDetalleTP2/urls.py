from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('gestionCabecera/', views.gestionCabecera),
    path('agregarCabecera/', views.agregarCabecera),
    path('gestionDetalle/', views.gestionDetalle),
    path('agregarDetalle/', views.agregarDetalle),
]