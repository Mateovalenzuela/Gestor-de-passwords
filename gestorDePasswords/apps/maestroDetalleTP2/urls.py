from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('gestionCabecera/', views.gestionCabecera),
    path('agregarCabecera/', views.agregarCabecera),
    path('gestionDetalle/', views.gestionDetalle),
    path('agregarDetalle/', views.agregarDetalle),
    path('gestionProducto/', views.gestionProducto),
    path('agregarProducto/', views.agregarProducto),
    path('edicionProducto/<indice>', views.edicionProducto),
    path('editarProducto/', views.editarProducto),
    path('eliminarProducto/<indice>', views.eliminarProducto),
    path('seleccionarCabecera/<indice>', views.seleccionarCabecera),
    path('guardarFactura/', views.guardarFacturaEnBd),
    path('verTodasLasFacturas/', views.verTodasLasFacturas),
    path('seleccionarFactura/<indice>', views.seleccionarFactura),
    path('modificacionFactura/', views.modificacionDeFactura),
    path('modificarFactura/', views.modificarFactura),
    path('modificarProducto/', views.modificarProducto),
    path('modificacionProducto/<indice>', views.modificacionProducto)
]