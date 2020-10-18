# ao chamar a funcao desta forma abaixo:
# todas as funções daquele módulo ficam no objeto que foi importado
# from module import funcoes
# funcoes.hello_world()

# importar funcao individualmente
from module.funcoes import hello_world
hello_world()

# as funções no python devem estar declaradas antes delas serem chamadas

# valores padrão são suportadas
def sumNumbers(a = 10, b = 12):
    return a+b 

# resultado: 7
print(sumNumbers(5, 2))

# resultado: 13
print(sumNumbers(1))

# resultado: 22
print(sumNumbers())

# passar somente segundo parametro
# podemos usar parametros nomeados
# resultado: 20
print(sumNumbers(b = 10))