# o operado in verifica se o elemento está presente em uma lista 

if 3 in {1,3,5,7}:
    print('Está contido')

# a função range retorna uma lista 
# os parametros são de onde inicia e até onde vai 
# o ultimo elemento nao entra, assim o ultimo elemento é o numero colocado menos 1 

# vai de 1 até 999
if 1000 in range(1, 1000):
    print('Está contido')
else:
    print('Não está contido')

# o range pode ser de 2 em 2, de 3 em 3, aí por diante
# basta colocar o numero a ser acrescentado, assim o intervalo ficará diferente
if 4 in range(0, 10, 4):
    print('4 contido')

# o range pode ir de forma decrescente também 

if 40 in range(100, 1, -1):
    print('40 contido de 100 a 1')


if 10 and 20 in range(0, 100, 10):
    print('10 e 20 contidos')
