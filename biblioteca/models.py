from django.db import models
from django.utils import timezone
from datetime import timedelta

# BANCO DE DADOS USUÁRIO
class Pessoa(models.Model):
    TIPO_CHOICES = (
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
    )

    nome = models.CharField(max_length=100)
    usuario = models.CharField(max_length=10, choices=TIPO_CHOICES)
    turma = models.CharField(max_length=50, blank=True) 

    def __str__(self):
        return f"{self.nome} ({self.usuario})"
    
# BANCO DE DADOS LIVROS EMPRESTADOS
class Emprestimo(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    devolvido = models.BooleanField(default=False)
    data_emprestimo = models.DateField(default=timezone.now)
    data_devolucao_prevista = models.DateField(default=timezone.now() + timedelta(days=7))

def save(self, *args, **kwargs):
    if not self.data_devolucao_prevista:
        self.data_devolucao_prevista = self.data_emprestimo + timedelta(days=7)
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.titulo} emprestado para {self.pessoa.nome}"


