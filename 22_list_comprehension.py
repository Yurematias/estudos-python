# list comprehension são formas de trabalhar com arrays 
# semelhante ao uso de maps, filters e etc.

alunos = [
  {'nome': 'Crocodile', 'nota':  7.8},
  {'nome': 'Doflamingo', 'nota':  5.5},
  {'nome': 'Kuma', 'nota':  6.3},
  {'nome': 'Jinbei', 'nota': 9.1},
]

# cria uma lista de alunos somente com o nome
# funciona igual um map
notas_alunos = [aluno['nome'] for aluno in alunos]
# equivale a:
# notas_alunos = list(map(lambda aluno: aluno['nome'], alunos))

print(notas_alunos) # resultado: ['Frodo', 'Naruto', 'Luffy', 'Picollo', 'Eren']

# funciona como um map junto com um filter
notas_alunos_aprovados = [aluno['nota'] for aluno in alunos if aluno['nota'] > 7]
# equivale a 
# notas_alunos_aprovados = list(filter(lambda nota: nota > 7, map(lambda aluno: aluno['nota'], alunos)))


print(notas_alunos_aprovados) # resultado: ['Frodo', 'Naruto', 'Luffy', 'Picollo', 'Eren']
