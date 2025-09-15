from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('producto/<slug:slug>/', views.detalle_producto, name='detalle'),
    path('categoria/<slug:slug>/', views.categoria_detalle, name='categoria'),
]