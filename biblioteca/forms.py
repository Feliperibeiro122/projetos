from django import forms
from biblioteca.models import Pessoa, Emprestimo

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'tipo', 'turma']

class EmprestimoForm(forms.ModelForm):
    nome_pessoa = forms.CharField(label="Nome do aluno/professor", max_length=100)

    class Meta:
        model = Emprestimo
        fields = ['titulo', 'descricao', 'pessoa']
