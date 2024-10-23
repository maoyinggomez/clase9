print("_______________________________________________________________________")
print("Acitividad #1")
def operar(a, b):
    suma = a + b
    if type(a) == type(b) and type(a) in [int, float]:
        resta = a - b
        multiplicacion = a * b
        division = a / b
        return suma, resta, multiplicacion, division
    else:
        return suma, None, None, None

print(operar(10, 2))
print(operar(10.0, 2))
print(operar("Hola", " Univalle"))
print(operar([1, 2], [3, 4]))


print("_______________________________________________________________________")
print("Acitividad #2")
class Vehiculo:
    def mover(self):
        pass

class Carro(Vehiculo):
    def mover(self):
        return 'El carro está conduciendo'

class Moto(Vehiculo):
    def mover(self):
        return 'La moto está conduciendo'

class Monopatin(Vehiculo):
    def mover(self):
        return 'El monopatín está rodando'


vehiculos = [Carro(), Moto(), Monopatin()]
for vehiculo in vehiculos:
    print(vehiculo.mover())
print("_______________________________________________________________________")
print("Acitividad #3")
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sumar(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

    def __repr__(self):
        return f'Punto({self.x}, {self.y})'

p1 = Punto(1, 2)
p2 = Punto(3, 4)
p3 = p1.sumar(p2)
print(p3)  
