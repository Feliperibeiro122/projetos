from django.shortcuts import render, redirect, get_object_or_404
from biblioteca.models import Emprestimo, Pessoa
from biblioteca.forms import PessoaForm, EmprestimoForm
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro')
    else:
        form = PessoaForm()

    return render(request, 'cadastro.html', {'form': form})

from .models import Emprestimo, Pessoa
from django.shortcuts import render, redirect

def emprestimo(request):
    if request.method == 'POST':
        nome = request.POST.get('nome_pessoa')
        pessoa = Pessoa.objects.filter(nome__iexact=nome).first()
        if pessoa:
            Emprestimo.objects.create(
                titulo=request.POST.get('titulo'),
                descricao=request.POST.get('descricao'),
                pessoa=pessoa
            )
            return redirect('emprestimo')

    # ⬇️ ESSA LINHA É FUNDAMENTAL
    emprestimos = Emprestimo.objects.all().order_by('-data_emprestimo')

    return render(request, 'emprestimo.html', {
        'emprestimos': emprestimos
        })



def buscar_pessoas(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        termo = request.GET.get('term', '')
        pessoas = Pessoa.objects.filter(nome__icontains=termo)
        nomes = list(pessoas.values_list('nome', flat=True))
        return JsonResponse(nomes, safe=False)
    
def devolver_livro(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)
    emprestimo.devolvido = True
    emprestimo.save()
    return redirect('emprestimo')