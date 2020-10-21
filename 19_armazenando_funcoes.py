def soma(a, b):
    return a+b

# no python é possível armazenar funcoes em variaveis assim como no js
somar = soma

print(somar(10, 7))

def operacao_aritmetica(fn, a, b):
    return fn(a, b)

print(operacao_aritmetica(somar, 2, 9))

# tambem é possivel retornar uma funcao
def subtracao(a):
    def concluir_subtracao(b):
        return a-b
    return concluir_subtracao

print(subtracao(10)(3))