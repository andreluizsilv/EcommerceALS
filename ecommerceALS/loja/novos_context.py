from django.db.models import Sum
from .models import Pedido, ItensPedido

def carrinho(request):
    qtd_prod_carrinho = 0
    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, criado = Pedido.objects.get_or_create(cliente=cliente, finalizado=False)
        resultado = ItensPedido.objects.filter(pedido=pedido).aggregate(total=Sum('quantidade'))
        qtd_prod_carrinho = resultado['total'] or 0
    return {"qtd_prod_carrinho": qtd_prod_carrinho}


