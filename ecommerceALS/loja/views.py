from django.shortcuts import render
from .models import *
# Create your views here.
def homepage(request):
    banners = Banner.objects.filter(ativo=True)
    context = {'banners': banners}
    return render(request,'homepage.html', context)


def loja(request, nome_departamento= None):
    produtos = Produto.objects.filter(ativo=True)
    if nome_departamento:
        produtos = produtos.filter(departamento__nome=nome_departamento)
        print(produtos)
    context = {'produtos': produtos}
    return render(request,'loja.html', context)

def carrinho(request):
    return render(request,'carrinho.html')

def checkout(request):
    return render(request,'checkout.html')



def minha_conta(request):
    return render(request,'usuario/minha_conta.html')


def login(request):
    return render(request,'usuario/login.html')






