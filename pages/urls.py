from django.urls import path
from django.views.generic import RedirectView

from . import views
from .views import *

urlpatterns = [
    path('', RedirectView.as_view(url='orquestrador/'), name='index'),
    path('orquestrador/', views.table_orquestrador, name='orquestrador'),

    path('cadastrar/robo/', CreateRobo.as_view(), name='cadastrar_robo'),
    path('cadastrar/vm/', CreateVm.as_view(), name='cadastrar_vm'),

    path('atualizar/robo/<int:pk>', UpdateRobo.as_view(), name='atualizar_robo'),
    path('atualizar/vm/<int:pk>/', UpdateVm.as_view(), name='atualizar_vm'),
    path('update-status/robo/<int:pk>', views.update_status, name='update_status'),	

    path('deletar/robo/<int:pk>/', DeleteRobo.as_view(), name='deletar_robo'),
    path('deletar/vm/<int:pk>/', DeleteVm.as_view(), name='deletar_vm'),
]
