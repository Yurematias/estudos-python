# para ler dados é muito fácil
variavel = input()
print(f'A variavel lida é {variavel}')
# no entando o input sempre retornara uma string 
# para forçalo a ler int ou outro tipo 
# precisamos...
var = int(input())
print('a variavel {} multiplicada por 2 é = {}'.format(var, var*2))
/
# também podemos imprimir um valor no momento da leitura para isso...
idade = int(input('Digite sua idade: ')) 