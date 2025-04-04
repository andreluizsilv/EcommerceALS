from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name="homepage"),

    path('loja/', loja, name="loja"),
    path('loja/<str:nome_departamento>/', loja, name="loja"),

    path('minhaconta/', minha_conta, name="minha_conta"),
    path('login/', login, name="login"),
    path('checkout/', checkout, name="checkout"),
    path('carrinho/', carrinho, name="carrinho"),
    path('adicionarcarrinho/<int:id_produto>/', adicionar_carrinho, name="adicionar_carrinho"),
    path('retirandoitemcarrinho/<int:id_produto>/', remover_carrinho, name="remover_carrinho"),

]
