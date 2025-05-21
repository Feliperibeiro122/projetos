from django.db import models

class Pessoa(models.Model):
    TIPO_CHOICES = (
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
    )

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    turma = models.CharField(max_length=50, blank=True) 

    def __str__(self):
        return f"{self.nome} ({self.tipo})"
    
class Emprestimo(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    devolvido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.titulo} emprestado para {self.pessoa.nome}"


