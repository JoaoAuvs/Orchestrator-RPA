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
        qdt_falha = []
        qdt_desativado = []
        qdt_desenvolvimento = []
        grupos = []
        for grupo in request.user.groups.all(): grupos.append(grupo.name)
        for indice, valor in enumerate(lista):
            if valor.departamento.name in grupos or request.user.is_staff:
                dashboard[indice] = {
                    'id': valor.id,
                    'nome': valor.nome,
                    'nome_alternativo': valor.nome_alternativo,
                    'departamento': valor.departamento.name,
                    'vm': valor.vm.nome_vm,
                    'hora_execucao': valor.hora_execucao,
                    'status': valor.status,
                }
            else:
                pass
            if valor.status == 'FALHA': qdt_falha.append(+1)
            if valor.status == 'DESATIVADO': qdt_desativado.append(+1)
            if valor.status == 'EM DESENVOLVIMENTO': qdt_desenvolvimento.append(+1)
        return render(request, "pages/orquestrador.html", {
            "robos": dashboard,
            "lista_falhas": qdt_falha,
            "lista_desativados": qdt_desativado,
            })
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
