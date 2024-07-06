from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "todos/home.html")


def todoListar(request):
    tarefas = [{
        'id':'1',
        'Tarefa':'comprar fraldas'
    }]
    return render(request, "todos/todolistar.html",{'tarefas':tarefas})
