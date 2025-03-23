from django.shortcuts import render, get_object_or_404, redirect
from .models import *
# Create your views here.
def homepage(request):
    banners = Banner.objects.filter(ativo=True)
    context = {'banners': banners}
    return render(request,'homepage.html', context)


def loja(request, nome_departamento=None):
    departamentos = Departamento.objects.prefetch_related('produtos').all()

    if nome_departamento:
        produtos = Produto.objects.filter(departamento__nome=nome_departamento, ativo=True)
    else:
        produtos = Produto.objects.filter(ativo=True)

    context = {
        'departamentos': departamentos,
        'produtos': produtos
    }
    return render(request, 'loja.html', context)

def ver_produto(request, id_produto):
    produto = get_object_or_404(Produto, id=id_produto)
    itens_estoque = ItemEstoque.objects.filter(produto=produto, quantidade__gt=0)

    # Verifica se há itens em estoque
    if itens_estoque.exists():
        quantidade_disponivel = sum(item.quantidade for item in itens_estoque)
        itens_estoque = True
    else:
        quantidade_disponivel = 0
        itens_estoque = False
    context = {
        'produto': produto,
        'itens_estoque': itens_estoque,
        'quantidade_disponivel': quantidade_disponivel,
    }
    return render(request, 'ver_produto.html', context)


def adicionar_carrinho(request, id_produto):
    if request.method == "POST" and id_produto:
        print("Enviou Formulario")
        return redirect('carrinho')
    else:
        return redirect('loja')  # Adicionado o 'return'


def carrinho(request):
    return render(request,'carrinho.html')

def checkout(request):
    return render(request,'checkout.html')



def minha_conta(request):
    return render(request,'usuario/minha_conta.html')


def login(request):
    return render(request,'usuario/login.html')






