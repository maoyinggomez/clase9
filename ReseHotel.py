class Habitacion:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo

class Reserva:
    def __init__(self, numeroReserva, habitacion, huesped):
        self.numeroReserva = numeroReserva
        self.habitacion = habitacion
        self.huesped = huesped

class ControlHotel:
    def __init__(self, cantidadHabitaciones):
        self.habitaciones = [Habitacion(numero, "doble" if numero % 2 == 0 else "individual") for numero in range(1, cantidadHabitaciones + 1)]
        self.reservas = []

    def realizarReserva(self, numeroReserva, numeroHabitacion, huesped):
        habitacion = self.habitaciones[numeroHabitacion - 1]

        # Comprobar si ya hay una reserva para esta habitación
        if any(reserva.habitacion.numero == habitacion.numero for reserva in self.reservas):
            print("La habitación ya está ocupada.")
        else:
            reserva = Reserva(numeroReserva, habitacion, huesped)
            self.reservas.append(reserva)
            print(f"Reserva realizada exitosamente para el huésped {huesped} en la habitación {habitacion.numero}.")

    def cancelarReserva(self, numeroReserva):
        for reserva in self.reservas:
            if reserva.numeroReserva == numeroReserva:
                self.reservas.remove(reserva)
                print("Reserva cancelada.")
                return
        print("No se encontró la reserva.")

    def listarHabitacionesDisponibles(self):
        habitacionesDisponibles = [habitacion for habitacion in self.habitaciones 
                                   if not any(reserva.habitacion.numero == habitacion.numero for reserva in self.reservas)]
        print("Habitaciones disponibles:")
        for habitacion in habitacionesDisponibles:
            print(f"Habitación {habitacion.numero} ({habitacion.tipo})")

controlHotel = ControlHotel(10)  

controlHotel.realizarReserva(1, 2, "Mao Gómez Uribe")

controlHotel.listarHabitacionesDisponibles()

controlHotel.cancelarReserva(1)

controlHotel.listarHabitacionesDisponibles()
