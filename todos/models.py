from django.db import models

# Create your models here.
class Todo(models.Model):
    titulo = models.CharField(max_length=150, null=False, blank=False)
    dtCriacao = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    dtFinalizado = models.DateTimeField(null=True)