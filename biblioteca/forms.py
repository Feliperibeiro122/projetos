from django import forms
from biblioteca.models import Pessoa, Emprestimo

# Formulário para usuário
class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'usuario', 'turma']

# Formulário para empréstimo
class EmprestimoForm(forms.ModelForm):
    nome_pessoa = forms.CharField(label="Nome do aluno/professor", max_length=100)

    class Meta:
        model = Emprestimo
        fields = ['titulo', 'descricao', 'pessoa']
