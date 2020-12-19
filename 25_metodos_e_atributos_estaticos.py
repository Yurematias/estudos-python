class Calculadora:
    # atributos declarados 
    # fora do 
    # construtor
    # pertencem a classe
    contador = 0

    # metodos da classe
    # difere um pouco do estatico
    # pertencem a classe
    # mas usam atributos da classe
    @classmethod
    def inc(cls):
        cls.contador += 1

    # os metodos estaticos
    # nao podem usar atributos 
    # da classe
    @staticmethod
    def somar(a, b):
        return a+b

print(Calculadora.somar(10, 4))
Calculadora.inc()
Calculadora.inc()
Calculadora.inc()
Calculadora.inc()
print(Calculadora.contador)