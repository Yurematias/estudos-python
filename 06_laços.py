lista = ['Geralt', 'Yennefer', 'Ciri', 'Tissaia', 'Emyr']

for item in lista:
    print(item) 

print('Indices e valores: ')
# para exibir os indices é necessario usar a função enumerate
for index, value  in enumerate(lista):
    print(f'{index}: {value}')

print('Usando range de 0 a 50, pulando de 10 em 10: ')
# usando range
for item in range(0, 50, 10):
    print(item)

print(print('Indices e valores, usando range de 0 a 50, pulando de 10 em 10'))
# hardcore não?
for index, value in enumerate(range(0, 50, 10)):
    print(f'{index}: {value}')

count = 1 

# while comum
while count <= 5:
    print(count)
    # o incremento não funciona com ++
    count += 1

count = 0

print('----------------------')

# pula o 3 por causa do continue
while count < 10:
    count += 1
    if count == 3: 
        continue
    print(count)


print('--------------------------------------')

# while-else e for-else 
# são executados assim que o laço termina

for item in lista: 
    print(item)
else:
    print('terminou o laço')

print('Testando laço')

for i in range(0, 10):
    # o end especifica o caracter ao final do print
    # neste caso será um espaço
    # por padrão no final do print acontece a quebra de linha
    print(i, end=' ')
else:
    print('Fim')