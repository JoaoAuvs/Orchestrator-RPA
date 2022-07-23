from datetime import datetime

from django.contrib.auth.models import Group, User
from django.db import models


class Vm(models.Model):
    nome_vm = models.CharField(max_length=35, null=False, blank= False)
    ip = models.CharField(max_length=35, null=False, blank= False)

    def __str__(self):
        return self.nome_vm

class Robo(models.Model):
    class Status(models.TextChoices):
        OPERACIONAL = 'OPERACIONAL', 'OPERACIONAL'
        EXECUTANDO = 'EXECUTANDO', 'EXECUTANDO'
        CONCLUIDO = 'CONCLUÍDO', 'CONCLUÍDO'
        FALHA = 'FALHA', 'FALHA'
        DESATIVADO = 'DESATIVADO', 'DESATIVADO'

    nome = models.CharField(max_length=100, null=False, blank=False)
    nome_alternativo = models.CharField(max_length=100, null=False, blank=False)
    departamento = models.ForeignKey(Group, on_delete=models.PROTECT)
    vm = models.ForeignKey(Vm, on_delete=models.PROTECT)
    hora_execucao = models.DateTimeField(null=False, blank=False,default= datetime.now)
    status = models.CharField(max_length=200, choices=Status.choices, default=Status.OPERACIONAL)

    def __str__(self):
        return self.nome
