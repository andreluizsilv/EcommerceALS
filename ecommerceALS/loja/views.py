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



def carrinho(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, criado = Pedido.objects.get_or_create(cliente=cliente, finalizado=False)
        itens_pedidos = ItensPedido.objects.filter(pedido=pedido)
        context = {'itens_pedidos': itens_pedidos, 'pedido': pedido}
    return render(request,'carrinho.html', context)


def adicionar_carrinho(request, id_produto):
    if request.method == "POST":
        try:
            quantidade = int(request.POST.get('quantidade', 1))
            if request.user.is_authenticated:
                cliente = request.user.cliente
            else:
                return redirect('login')
            item_estoque = ItemEstoque.objects.get(produto__id=id_produto)
            pedido, criado = Pedido.objects.get_or_create(cliente=cliente,finalizado=False)
            item_pedido, criado = ItensPedido.objects.get_or_create(pedido=pedido, item_estoque=item_estoque, defaults={'quantidade': quantidade})
            if not criado:
                item_pedido.quantidade += quantidade
                item_pedido.save()
            return redirect('carrinho')
        except ItemEstoque.DoesNotExist:
            return redirect('loja')
        except Exception as e:
            return redirect('loja')
    return redirect('loja')


def remover_carrinho(request):
    if request.method == "POST":
        try:
            quantidade = int(request.POST.get('quantidade', 1))
            if request.user.is_authenticated:
                cliente = request.user.cliente
            else:
                return redirect('login')
            item_estoque = ItemEstoque.objects.get(produto__id=id_produto)
            pedido, criado = Pedido.objects.get_or_create(cliente=cliente,finalizado=False)
            item_pedido, criado = ItensPedido.objects.get_or_create(pedido=pedido, item_estoque=item_estoque, defaults={'quantidade': quantidade})
            if not criado:
                item_pedido.quantidade -= quantidade
                item_pedido.save()
            return redirect('carrinho')
        except ItemEstoque.DoesNotExist:
            return redirect('loja')
        except Exception as e:
            return redirect('loja')
    return redirect('loja')


def checkout(request):
    return render(request,'checkout.html')



def minha_conta(request):
    return render(request,'usuario/minha_conta.html')


def login(request):
    return render(request,'usuario/login.html')






