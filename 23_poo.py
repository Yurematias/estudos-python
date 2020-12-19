#!python3
from random import randint

class Produto:
    # o __init__ é o construtor da classe
    # o self sempre recebe a própria referência da classe, é como se fosse o this
    # o self é recebido automaticamente ao instanciar, não é preciso passar por parâmetro
    def __init__(self, nome, preco, quantidade = 1):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        # é possível criar atributos privados 
        # para isso é só colocar __ antes do nome da variável
        # os atributos são realmente privados
        # não é só uma convenção como no javascript
        # no entanto ainda é possível forçar a barra 
        # e acessá-los usando nome_objeto._NomeDaClasse__nome_atributo_privado
        # exemplo: _Produto__codigo
        self.__codigo_produto = randint(0, 1000000)
 
    # o self precisa estar em todos os métodos
    # mesmo não precisando passalo, ele é recebido automaticamente
    def get_preco_total_unidades(self):
        return self.quantidade * self.preco
    # o propertu é semelhante ao get do javascript
    # ele faz com que seja pego um valor como se fosse 
    # um atributo
    # é como se fosse o computed do vue
    @property
    def preco_com_promocao(self):
        print('executou preco com promocao')
        return self.preco * 0.8
    
    @property
    def codigo_produto(self):
        print('usando getter de __codigo_produto')
        return self.__codigo_produto

    # declarando setter
    # só é possível se existir um getter de mesmo nome
    @codigo_produto.setter
    def codigo_produto(self, novo_cod):
        if novo_cod > 0 and novo_cod < 1000000:
            self.__codigo_produto = novo_cod

# instanciando objetos
# não utiliza o new
produto = Produto('Playstation 5', 4800, 7)

print(produto.nome)
print(produto.preco)
print(produto.quantidade)
print(produto.codigo_produto)
print(f'preco total: {produto.get_preco_total_unidades()}')
print('preco com promocao: ', produto.preco_com_promocao)


# não é possível acessar atributos privados 
# print(produto.__codigo_produto) # resulta em erro

# forçando a barra para acessar atributos privados
# isto não é recomendado 
# tanto que o autocomplete nem sugere
# print(produto._Produto__codigo_produto)

# alterando valor com setter 
produto.codigo_produto = 10
print('novo codigo: ', produto.codigo_produto)

# nao altera por conta da regra de negocio do setter
produto.codigo_produto = -1
print('novo codigo: ', produto.codigo_produto)

