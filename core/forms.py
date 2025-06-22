from django import forms
from .models import Tarefas


class TarefasForm(forms.ModelForm):
    class Meta:
        model = Tarefas
        fields = ['titulo', 'descricao', 'status']
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite o título da tarefa'
                }
            ),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descreva sua tarefa'
            }),
            'concluida': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
