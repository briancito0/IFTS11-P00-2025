from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('perros/', views.listar_perros, name='listar_perros'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('adoptar/<int:perro_id>/', views.adoptar_perro, name='adoptar_perro'),
]