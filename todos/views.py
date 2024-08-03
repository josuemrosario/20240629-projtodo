from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from django.views.generic import ListView, CreateView,UpdateView, DeleteView,View
from django.urls import reverse_lazy

from datetime import date
from django.shortcuts import redirect

#imports utilizados no sistema de login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout  
from django.contrib.auth.mixins import LoginRequiredMixin


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

class todoListarView(LoginRequiredMixin, ListView):
    model = Todo #classe deve usar o modelo ToDo (.\todos\models.py)

class todoCriarView(LoginRequiredMixin,CreateView):
    model = Todo
    fields = ["titulo","dtFinalizado"]  # Uma lista de campos que o usuario pode alterar
    success_url = reverse_lazy('todo_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Adicionar Tarefa'
        return context

class todoAtualizarView(LoginRequiredMixin,UpdateView):
    model = Todo
    fields = ["titulo","dtFinalizado"]  # Uma lista de campos que o usuario pode alterar
    success_url = reverse_lazy('todo_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Atualizar Tarefa'
        return context
    
class todoDeletarView(LoginRequiredMixin,DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_listar')

class todoCompletarView(LoginRequiredMixin,View):
    def get(self,request,pk):
        tarefa = Todo.objects.get(pk=pk)
        tarefa.dtFinalizado = date.today()
        tarefa.save()
        return redirect('todo_listar')

def todoCadastrarView(request):
    if request.method == "GET":
        contexto = {
            'titulo_pagina': 'Cadastrar Usuário'
        }
        return render(request, "todos/cadastro.html",contexto)
    elif request.method == "POST":
        nome_usuario = request.POST['usuario']
        senha = request.POST['senha']
        
        try:
            if User.objects.get(username=request.POST['usuario']): 
                contexto = {
                    'titulo_pagina': 'Cadastrar Usuário',
                    'msg': 'Erro! usuário já existe'
                }   
                return render(request, "todos/cadastro.html", contexto)
        except User.DoesNotExist:
            #salva o usuário
            novoUsuario = User.objects.create_user(username=nome_usuario,email='',password=senha)
            novoUsuario.save()

        usuario = authenticate(username=nome_usuario,password=senha)

        return redirect('todo_listar')


def todoLoginView(request):
    if request.method == "GET":
        contexto = {
            'titulo_pagina': 'Login'
        }
        return render(request, "todos/cadastro.html",contexto)
    elif request.method == "POST":
        nome_usuario = request.POST['usuario']
        senha = request.POST['senha']
        try:
            if User.objects.get(username=request.POST['usuario']):  
                usuario = authenticate(username=nome_usuario,password=senha)  
                if usuario is not None:
                    login(request, usuario)
                    return redirect('todo_listar')
                else:
                    contexto = {
                        'titulo_pagina': 'Login',
                        'msg':'usuario ou senha inválidos'
                    }
                    return render(request, "todos/cadastro.html",contexto)
        except User.DoesNotExist:
            contexto = {
                'titulo_pagina': 'Login',
                'msg': 'Erro! usuário não existe por favor cadastre'
            }
            return render(request, "todos/cadastro.html",contexto)


def todoLogoutView(request):
    logout(request)
    return redirect('todo_listar')