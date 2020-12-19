#!python3

class Carro:
    def __init__(self):
        self.__velocidade = 0

    @property
    def velocidade(self):
        return self.__velocidade

    def acelerar(self):
        self.__velocidade += 5
        return self.__velocidade
    
    def desacelerar(self):
        self.__velocidade -= 5
        return self.__velocidade

# para uma classe herdar a outra
# passamos o nome da classe pai 
# entre parenteses
class Mustang(Carro):
    # override 
    def acelerar(self):
        super().acelerar()
        super().acelerar()
        super().acelerar()
        super().acelerar()

c1 = Carro()

c1.acelerar()
c1.acelerar()
c1.acelerar()
c1.acelerar()
c1.acelerar()
c1.desacelerar()
c1.desacelerar()
print(c1.velocidade)

v8 = Mustang()

v8.acelerar()
v8.acelerar()
v8.acelerar()
v8.acelerar()
v8.acelerar()
v8.desacelerar()
v8.desacelerar()
print(v8.velocidade)