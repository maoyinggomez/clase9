class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False

    def encender(self):
        self.encendido = True
        print(f"{self.marca} {self.modelo} encendido.")

    def apagar(self):
        self.encendido = False
        print(f"{self.marca} {self.modelo} apagado.")


class Auto(Vehiculo):
    def tocarPito(self):
        if self.encendido:
            print(f"{self.marca} {self.modelo} hace beep beep!")
        else:
            print(f"¡No puedes tocar el pito! El {self.marca} {self.modelo} está apagado.")


class Moto(Vehiculo):
    def picarla(self):
        if self.encendido:
            print(f"{self.marca} {self.modelo} picándola!")
        else:
            print(f"¡No puedes picar la moto! La moto {self.marca} {self.modelo} está apagada.")


class GestionFlota:
    def __init__(self):
        self.vehiculos = []

    def agregarVehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"Vehículo {vehiculo.marca} {vehiculo.modelo} agregado a la flota.")

    def listarVehiculos(self):
        if not self.vehiculos:
            print("No hay vehículos en la flota.")
        else:
            print("Vehículos en la flota:")
            for vehiculo in self.vehiculos:
                tipo = "Auto" if isinstance(vehiculo, Auto) else "Moto"
                estado = "encendido" if vehiculo.encendido else "apagado"
                print(f"{tipo}: {vehiculo.marca} {vehiculo.modelo} - Estado: {estado}")


gestionFlota = GestionFlota()

auto1 = Auto("Toyota", "Prado TXL")
moto1 = Moto("Pulsar", "NS-250")
gestionFlota.agregarVehiculo(auto1)
gestionFlota.agregarVehiculo(moto1)

auto1.encender()
moto1.encender()

auto1.tocarPito()
moto1.picarla()

gestionFlota.listarVehiculos()

auto1.apagar()
moto1.apagar()

gestionFlota.listarVehiculos()
