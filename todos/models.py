from django.db import models

# Create your models here.
class Todo(models.Model):
    titulo = models.CharField(verbose_name="Titulo da tarefa",max_length=150, null=False, blank=False)
    dtCriacao = models.DateTimeField(verbose_name="Data de Criação",auto_now_add=True, null=False, blank=False)
    dtFinalizado = models.DateTimeField(verbose_name="Data de Finalização",null=True, blank=True) 