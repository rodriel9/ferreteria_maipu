from django.urls import path
from . import views

app_name = 'carrito'

urlpatterns = [
    path('', views.ver_carrito, name='ver'),
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar'),
    path('actualizar/<int:item_id>/', views.actualizar_cantidad, name='actualizar'),
    path('eliminar/<int:item_id>/', views.eliminar_producto, name='eliminar'),
    path('limpiar/', views.limpiar_carrito, name='limpiar'),
    path('count/', views.carrito_count, name='count'),
]