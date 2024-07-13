"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
# from todos.views import home, todoListar
from todos.views import todoListarView,todoCriarView

urlpatterns = [
    path("admin/", admin.site.urls),
    # rota que lista as tarefas
    # path("", todoListar),
    path("", todoListarView.as_view(template_name="todos/todolistar.html"),name='todo_listar'),   
    path("criar", todoCriarView.as_view(),name='todo_criar')
]
