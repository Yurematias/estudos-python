#!python3

# o método reduce não está disponível por 
# padrão no python, portanto precisa ser importado
from functools import reduce

notas = [7.4, 5.5, 10]

def somar(a, b):
    return a + b

soma = reduce(somar, notas)

# para começar com um valor só passar o terceiro parametro
# soma = reduce(somar, notas, 10)

print(f'Média: {soma / len(notas)}')

def aumentar_nota(a):
    final = a + 1
    return final if final < 10 else 10

# o map do python já vem por padrão

'''
OBSERVAÇÃO: A partir do python 3 o map não retorna uma lista
            e sim um iterable, desta forma precisamos colocar o 
            resultado num list() para converter
            assim como é feito no Dart com o 'as List'
'''
notas_com_ponto_extra = list(map(aumentar_nota, [7, 8, 6]))

print(notas_com_ponto_extra)

# usando programação funcional
def diminuir_nota(delta: float or int):
    def calcular(nota):
        return nota - delta
    return calcular

notas_reduzida = list(map(diminuir_nota(1), (10, 9, 8.5)))

print(f'Notas originais: ${(10, 9, 8.5)}')
print(f'Notas reduzidas em 1 ponto: {notas_reduzida}')
