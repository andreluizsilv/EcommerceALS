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
        for item in itens_pedidos:
            print(item.quantidade)
        context = {'itens_pedidos': itens_pedidos, 'pedido': pedido}
    return render(request,'carrinho.html', context)


def adicionar_carrinho(request, id_produto):
    if request.method == 'POST':
        quantidade = int(request.POST.get('quantidade', 1))

        item_estoque = ItemEstoque.objects.get(id=id_produto)

        # Busca ou cria um pedido em andamento para o cliente
        pedido, _ = Pedido.objects.get_or_create(cliente=request.user.cliente, finalizado=False)

        # Busca ou cria um item no pedido
        item_pedido, item_criado = ItensPedido.objects.get_or_create(
            pedido=pedido,
            item_estoque=item_estoque,
            defaults={'quantidade': quantidade}
        )

        if not item_criado:
            item_pedido.quantidade += quantidade
            item_pedido.save()

        return redirect('carrinho')


def remover_carrinho(request, id_produto):
    if request.method == 'POST':
        quantidade = int(request.POST.get('quantidade', 1))

        item_estoque = ItemEstoque.objects.get(id=id_produto)
        pedido = Pedido.objects.get(cliente=request.user.cliente, finalizado=False)

        item_pedido, item_criado = ItensPedido.objects.get_or_create(
            pedido=pedido,
            item_estoque=item_estoque,
            defaults={'quantidade': 0}
        )

        if not item_criado:
            item_pedido.quantidade -= quantidade
            if item_pedido.quantidade <= 0:
                item_pedido.delete()
            else:
                item_pedido.save()

        return redirect('carrinho')


def checkout(request):
    return render(request,'checkout.html')



def minha_conta(request):
    return render(request,'usuario/minha_conta.html')


def login(request):
    return render(request,'usuario/login.html')






