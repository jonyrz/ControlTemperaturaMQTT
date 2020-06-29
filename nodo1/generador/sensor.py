

class Sensor:
    def __init__(self, habitacion):
        self.habitacion = habitacion

    def leer(self, t, dt):
        T1 = self.habitacion.read(t)
        T2 = self.habitacion.read(t + dt)
        return (T1 + T2) / 2