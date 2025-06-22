from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefas
from .forms import TarefasForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'core/index.html')

@login_required
def cadastrarTarefa(request):
    if request.method == 'POST':
        form = TarefasForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.usuario = request.user
            tarefa.save()
            return redirect('listarTarefas')
    else:
        form = TarefasForm()
    
    return render(request, 'core/cadastrarTarefa.html', {'form': form})

@login_required
def listarTarefas(request):
    tarefas = Tarefas.objects.filter(usuario=request.user)
    return render(request, 'core/listarTarefas.html', {'tarefas': tarefas})

def tarefaDetalhe(request, pk):
    tarefa = get_object_or_404(Tarefas, pk=pk, usuario=request.user)
    return render(request, 'core/tarefaDetalhe.html', {'tarefa': tarefa})

@login_required
def editarTarefa(request, pk):
    tarefa = get_object_or_404(Tarefas, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = TarefasForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('tarefaDetalhe', pk=tarefa.id)
    else:
        form = TarefasForm(instance=tarefa)
    return render(request, 'core/editarTarefa.html', {'form': form, 'tarefa': tarefa})

@login_required
def excluirTarefa(request, pk):
    tarefa = get_object_or_404(Tarefas, pk=pk, usuario=request.user)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('listarTarefas')
    
    return render(request, 'core/excluirTarefa.html', {'tarefa': tarefa})
