# upper
# lower()
# len()
# replace('str','str')
# count('str')
# find('str')
# title()

# retorna a string so que maiuscula 
print('yure matias'.upper())
# retorna a string so que minuscula 
print('YURE MATIAS DE OLIVEIRA'.lower())
# é uma função (não método) que retorna o tamanho da string passada 
print(len('Yure'))
# substitui um pedaço da strinf por outro pedaço 
print('YURE MATIAS'.replace('MATIAS', 'OLIVEIRA'))
# count retorna a quantidade de ocorrencia de uma string especifica 
print('A LETRA \'a\' APARECE {} VEZES EM Yure Matias de Oliveira'.format('Yure Matias de Oliveira'.count('a')))
# o find retorna a posiição onde se encontra a letra passada 
print('Yure Matias'.find('e')) 
# deixa o primeiro caracter maiusculo e o resto minusculo, ideal para nomes proprios 
print('YURE MATIAS'.title())
print('yure matias'.title())
print('yUrE mAtiAs'.title())

