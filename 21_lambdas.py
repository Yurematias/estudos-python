from functools import reduce

alunos = [
  {'nome': 'Frodo', 'nota':  7.8},
  {'nome': 'Naruto', 'nota':  5.5},
  {'nome': 'Luffy', 'nota':  6.3},
  {'nome': 'Picollo', 'nota': 9.1},
  {'nome': 'Eren', 'nota': 6.9},
]

# sintaxe da lambda:
# lambda aluno: aluno['nota'] >= 7

# aluno é o parametro a ser recebido
# depois dos : é a instrução de retorno


verificar_aprovacao = lambda aluno: aluno['nota'] >= 7

# o filter retorna um filter object 
# assim é preciso converter para uma lista
alunos_aprovados = list(filter(verificar_aprovacao, alunos))
print('alunos aprovados: ', alunos_aprovados)


# declarando funcao anonima com lambda dentro da chamada da filter
alunos_reprovados = list(filter(lambda aluno: aluno['nota'] < 7, alunos))
print('alunos reprovados: ', alunos_reprovados)

# usando com reduce 
media = reduce(lambda a,b: a+b, map(lambda aluno: aluno['nota'], alunos)) / len(alunos)

print(media)
