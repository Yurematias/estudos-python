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

# no python podemos definir uma tipagem nos parametros
# entretanto não funciona como no TypeScript
# podemos passar tipos diferentes
# a definição é só pra marcar o que deve ser feito
# o PEP (Python Enhancement Proposals) indica 
# que sejam usadas essas definições
# o Python pressupõe que você seja adulto
# o suficiente pra ver que a funcao recebe um tipo 
# e não mandar um tipo diferente
def juntar_strings(a: str, b: str):
    return f'{a}{b}'

print(juntar_strings('Yure ', 'Matias'))

# o código abaixo não dá erro, mas não é recomendado
# pois a funcao quer strings, não numeros 
print(juntar_strings(12, 54))

# forçar erro em argumentos de tipos errados
def juntar_strings_rigido(a: str, b: str):
    # isinstance verifica se determinado valor ou variavel
    # é instancia de uma classe, no caso abaixo verifica se são objetos de string
    if not isinstance(a, str) or not isinstance(b, str):
        # raise é tipo o throw new Error do JavaScript
        raise TypeError
    return f'{a}{b}'

# não dá erro, pois os parametros certos são enviados
print(juntar_strings_rigido('Monkey D. ', 'Luffy'))

# o código abaixo dá erro
# print(juntar_strings_rigido(1000, 4))