from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from requests import request

from .models import Robo, Vm

################ CREATE ################

class CreateRobo(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Robo
    fields = ['nome', 'nome_alternativo', 'departamento', 'vm', 'horario_execucao']

class CreateVm(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Vm
    fields = ['nome_vm', 'ip']

################ UPDATE ################

class UpdateRobo(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Robo
    fields = ['nome', 'nome_alternativo', 'departamento', 'vm', 'horario_execucao']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

class UpdateVm(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Vm
    fields = ['nome_vm', 'ip']

################ DELETE ################

class DeleteRobo(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Robo

class DeleteVm(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Vm

################ LISTAR ################

@login_required(login_url='/login/')
def table_orquestrador(request):
    try:
        lista = Robo.objects.all().order_by('nome')
        dashboard = {}
        grupos = []
        for grupo in request.user.groups.all(): grupos.append(grupo.name)
        for robo in lista:
            if robo.departamento.name in grupos or request.user.is_staff:
                dashboard[robo] = robo
            else:
                pass
        return render(request, "pages/orquestrador.html", {"robos": dashboard})
    except:
        print("A resposta não chegou com o formato esperado.")
        return render(request, "pages/orquestrador.html")

def update_status(request, pk):
    try:
        robo = Robo.objects.get(pk=pk)
        if robo.status == "OPERACIONAL":
            robo.status = "OFF"
        else:
            robo.status = "ON"
        robo.save()
        return render(request, "pages/dashboard.html")
    except:
        print("A resposta não chegou com o formato esperado.")
        return render(request, "pages/dashboard.html")
