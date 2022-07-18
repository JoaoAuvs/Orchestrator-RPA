from django.contrib.auth.models import Group, User
from django.db import models


class Vm(models.Model):
    nome_vm = models.CharField(max_length=35, null=False, blank= False)
    ip = models.CharField(max_length=35, null=False, blank= False)

    def __str__(self):
        return self.nome_vm

class Robo(models.Model):
    nome = models.CharField(max_length=100)
    nome_alternativo = models.CharField(max_length=100)
    departamento = models.ForeignKey(Group, on_delete=models.PROTECT)
    vm = models.ForeignKey(Vm, on_delete=models.PROTECT)
    hora_execucao = models.DateTimeField(blank=True, null=True, editable=False)
    status = models.CharField(max_length=100, default='OPERACIONAL')

    def __str__(self):
        return self.nome
