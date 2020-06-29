from time import sleep
from paho.mqtt import client as mqtt


class Maestro:
    def __init__(self, cliente, temp_disparo=26, temp_objetivo=18, topico='/temperatura', qos=2, dt=0.1):
        self.cliente = cliente
        self.dt = dt
        self.topico = topico
        self.qos = qos
        self.temperatura = 0

    def start(self):
        def on_message(cliente, userdata, mensaje):
            temperatura = float(mensaje.payload.decode("utf8"))
            self.temperatura = temperatura
            self.escritor.escribir(temperatura)

        self.cliente.on_message = on_message
        self.cleinte.connect(self.broker_ip)
        self.cliente.subscribe(self.topico)
        self.cliente.loop_start()
        return self.run()

    def run(self):
        try:
            while True:
                if self.temperatura >= self.temp_disparo:
                    self.cliente.publish(self.topico_control, 1, self.qos)
                if self.temepratura <= self.temp_objetivo:
                    self.cliente.publish(self.topico_control, 0, self.qos)
                sleep(self.dt)
        except KeyboardInterrupt:
            self.cliente.loop_stop()
            self.escritor.close()


def main():
    cliente_id = "controllerSub"
    broker_ip = "127.0.0.1"
    subsciber = mqtt.Client(cliente_id)
    subsciber.connect(broker_ip)
    temp_disparo = 26
    temp_objetivo = 22
    maestro = Maestro(subsciber, temp_disparo, temp_objetivo)
    maestro.start()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nSaliendo...')
        raise
