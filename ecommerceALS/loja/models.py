from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=200, null=True, blank=True)
    id_sessao = models.CharField(max_length=200, null=True, blank=True)
    usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.email if self.email else "Cliente sem email"

class Endereco(models.Model):
    rua = models.CharField(max_length=400, null=True, blank=True)
    numero = models.IntegerField(default=0)
    complemento = models.CharField(max_length=200, null=True, blank=True)
    cep = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    estado = models.CharField(max_length=200, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        cliente_info = self.cliente.email if self.cliente else "Sem Cliente"
        return f'{cliente_info} - {self.rua} - {self.cidade} - {self.estado} - {self.cep}'



class Departamento(models.Model): # Categoria: Acougue, Hortifruti, Padaria, etc.
    nome = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome

class Tipo(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)
    departamento = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'Produto: {self.nome}'


class Produto(models.Model):
    imagem = models.ImageField(null=True, blank=True)
    nome_produto = models.CharField(max_length=200, null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    unidade = models.CharField(max_length=200, null=True, blank=True)
    ativo = models.BooleanField(default=True)
    departamento = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.SET_NULL, related_name="produtos")
    tipo = models.ForeignKey(Tipo, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'Nome: {self.nome_produto} - Setor: {self.departamento} -  {self.tipo} - Preço: {self.preco} {self.unidade}'


class ItemEstoque(models.Model):
    produto = models.ForeignKey(Produto, null=True, blank=True, on_delete=models.SET_NULL)
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.produto.nome_produto}  - Quantidade: {self.quantidade}'

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)
    finalizado = models.BooleanField(default=False)
    codigo_transacao = models.CharField(max_length=200, null=True, blank=True)
    endereco = models.ForeignKey(Endereco, null=True, blank=True, on_delete=models.SET_NULL)
    data_finalizacao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Cliente: {self.cliente.email}   -  id_pedido:  {self.id} - Finalizado: {self.finalizado}"


class ItensPedido(models.Model):
    item_estoque = models.ForeignKey(ItemEstoque, null=True, blank=True, on_delete=models.SET_NULL)
    quantidade = models.IntegerField(default=0)
    pedido = models.ForeignKey(Pedido, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'IdProduto: {self.pedido.id} - Produto: {self.item_estoque.produto.nome_produto} - Preço: {self.item_estoque.produto.preco}{self.item_estoque.produto.unidade}'
class Banner (models.Model):
    imagem = models.ImageField(null=True, blank=True)
    link_destino = models.CharField(max_length=400, null=True, blank=True)
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return f" {self.link_destino}   -  Ativo:  {self.ativo}"
