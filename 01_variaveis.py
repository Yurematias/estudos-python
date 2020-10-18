print('---------------------------------------')
# em python váriavies não precisam ser declaradas

# existem dados do tipo 
# inteiro 
# boleano
# float 
# string

# strings podem ser declaradas com aspas simples ou duplas 
nome = 'Yure'
sobrenome = " Matias de Oliveira"

# forma de concatenar Strings 
print(nome + sobrenome)

idade = 19 

# existe uma forma de concatenar strings com variaveis 
# como se fosse template string do javascript 
# basta colocar um f antes da aspa
# assim o interpretador saberá que quando houver chaves 
# o valor impresso será de uma vari-avel 
print(f'Tenho {idade} anos')

# outra forma é usanddo o .format 
# format é um método de objetos String 
# esse método substitui as chaves da String pelos valores
# passados nos parametros
print('Eu tenho {} anos e sou {}'.format(19, 'brasileiro'))

# é possível fazer sem seguir a ordem 

print('Eu tenho {anos} anos e sou {nacionalidade}'.format(nacionalidade='brasileiro', anos=idade))

# a função type retorna o tipo da variável 
print(type('YURE'))
print(type(88))
print(type(56.3))
print(type(True)) # valores boleanos começam com letra maiúscula
