from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar_tarefa/', views.cadastrarTarefa, name='cadastrarTarefa'),
    path('listar_tarefas/', views.listarTarefas, name='listarTarefas'),
    path('tarefa_detalahe/<int:pk>/', views.tarefaDetalhe, name='tarefaDetalhe'),
    path('editar_tarefa/<int:pk>/', views.editarTarefa, name='editarTarefa'),
    path('excluir_tarefa/<int:pk>/', views.excluirTarefa, name='excluirTarefa'),
]
