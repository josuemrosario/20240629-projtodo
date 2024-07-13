from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy


# Create your views here.
def home(request):
    return render(request, "todos/home.html")

'''
def todoListar(request):
    # tarefas = [{
    #     'id':'1',
    #     'Tarefa':'comprar fraldas'
    # }]
    tarefas = Todo.objects.all()
    print(tarefas)
    return render(request, "todos/todolistar.html", {"tarefas": tarefas})
'''

class todoListarView(ListView):
    model = Todo #classe deve usar o modelo ToDo (.\todos\models.py)

class todoCriarView(CreateView):
    model = Todo
    fields = ["titulo","dtFinalizado"]  # Uma lista de campos que o usuario pode alterar
    success_url = reverse_lazy('todo_listar')