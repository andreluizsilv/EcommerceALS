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



def adicionar_carrinho(request, id_produto):
    if request.method == "POST" and id_produto:
        quantidade = request.POST.dict()
        print(quantidade, id_produto)
        return redirect('carrinho')
    else:
        return redirect('loja')  # Adicionado o 'return'


def carrinho(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, criado = Pedido.objects.get_or_create(cliente=cliente, finalizado=False)
        itens_pedidos = ItensPedido.objects.filter(pedido=pedido)
        context = {'itens_pedidos': itens_pedidos, 'pedido': pedido}
    return render(request,'carrinho.html', context)

def checkout(request):
    return render(request,'checkout.html')



def minha_conta(request):
    return render(request,'usuario/minha_conta.html')


def login(request):
    return render(request,'usuario/login.html')






