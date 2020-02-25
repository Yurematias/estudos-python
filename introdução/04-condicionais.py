variavel = int(input('Digite um valor para a variavel: '))

# o python não tem chaves, a identação é o que determina os escopos 

if variavel == 10:
    print('É IGUAL A 10')
elif variavel == 1000:
    print('NÃO É IGUAL A 10 MAS É IGUAL A 1000')
else:
    print('Não é igual a 10 nem a 1000')        

if variavel == 20 or variavel == 40:
    print('é igual a 20 ou 40')

elif variavel == 10 and variavel % 2 == 0:
    print('é igual a 10 e é divisivel por 2 obviamente né...')

# o operador not é o ~
# embora o de diferente continue sendo !

if ~(5 != 5):
    print('entrou na condição')