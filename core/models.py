from django.db import models
from django.contrib.auth.models import User

class Tarefas(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pendente'),
        ('C', 'Concluído'),
    ]

    titulo = models.CharField(max_length=20)
    descricao = models.TextField(blank=True)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='P'
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.titulo} ({self.get_status_display()})'
    
