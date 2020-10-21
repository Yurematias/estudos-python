# os valores vem como uma tupla
# é o equivalente à ...numbers jo JavaScript
def sumList(*numbers):
    # type = tupla
    print(type(numbers)) 
    result = 0
    for i in numbers:
        result += i
    return result


print(sumList(12, 10, 5, 10, 2))


# recebendo dicionario (Map) no parametro
# kwargs = key word args
def showStudantData(**studant):
    # type = dicionario
    print(type(studant))
    print(studant['name'])
    print(studant['age'])
    print(studant['school'])

showStudantData(
    name = 'Yure',
    age = 20,
    school = 'EAJ',
)