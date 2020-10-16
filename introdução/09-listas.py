
# há 2 formas de declarar uma lista

times_br = []

# ou

times_arg = list()
times_arg.append('Boca Juniors')
times_arg.append('River Plate')
times_br = ['Corinthians', 'Flamengo', 'Grêmio', 'Atlétio Mineiro']

# é possivel juntar duas listas com o +
times_sul_americanos = times_br + times_arg

print(times_sul_americanos)

# o vezes multiplica a quantidade de cada um dos itens na lista
print(f'times argentinos repetidos {times_arg * 3}')

# o pop funciona normalmente porem quando passado um indice
# ele remove o elemento do indice passado
times_br.pop(1)
# imprime sem o Flamengo
print(times_br) 

# sem passar valor, o pop tira o ultimo, assim como em pilhas
times_br.pop()
# imprime sem o Atlético
print(times_br) 

# o remove remove pelo valor e não por indice
times_br.remove('Grêmio')
# imprime sem o Grêmio
print(times_br) 

lista = [2, 34, 1, 45, 100, 12, 3]

print('Antes: ', lista)

lista.sort()

print('Depois: ', lista)

lista2 = [2, 34, 1, 45, 100, 12, 3]
print('Antes: ', lista2)

# parametro nomeado reverse faz o sort inverter
lista2.sort(reverse=True)

print('Depois: ', lista2)

# imprimir valor máximo da lista
print(max(lista))

# imprimir valor mínimo da lista
print(min(lista))

# imprimir soma dos valores da lista
print(sum(lista))

# forma de fazer uma lista grande rapidamente
lista_grande = list(range(1, 501))
print(lista_grande)