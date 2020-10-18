try: 
    idade = int(input('Digite a idade: '))
except:
    print('Você não digitou a idade de forma correta')
else:
    print(f'Daqui a 2 anos você terá {idade+2}')