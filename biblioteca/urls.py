from django.urls import path
from biblioteca.views import index,cadastro,emprestimo,buscar_pessoas, devolver_livro

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('emprestimo/', emprestimo, name='emprestimo'),
    path('buscar-pessoas/', buscar_pessoas, name='buscar_pessoas'),
    path('devolver/<int:emprestimo_id>/', devolver_livro, name='devolver'),
]
