from paho.mqtt import client as mqtt
# from cliente import Cliente
from threading import Thread
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import sleep


class Maestro:
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    q = []

    def __init__(self, cliente, datos, broker_ip='127.0.0.1', cliente_id='bogar', topico='/temperatura', qos=2, dt=0.1):
        self.dt = dt
        self.topico = topico
        self.qos = qos
        self.sleep_time = 0.5
        self.client_id = cliente_id
        self.broker_ip = broker_ip
        self.cliente = cliente
        self.datos = datos

    def start(self):
        return self.run()

    def run(self):
        def on_message(cliente, userdata, mensaje):
            temperatura = float(mensaje.payload.decode("utf8"))
            self.datos.append(temperatura)
        self.cliente.on_message = on_message
        self.cliente.connect(self.broker_ip)
        self.cliente.subscribe(self.topico)
        self.cliente.loop_start()
        while True:
            sleep(self.dt)


def main():
    datos = []
    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    def animate(index):
        ax1.clear()
        ax1.plot(datos[::])
    cliente_id = "graficaSub"
    cliente = mqtt.Client(cliente_id)
    maestro = Maestro(cliente, datos)
    t = Thread(target=maestro.start)
    t.start()
    ani = animation.FuncAnimation(fig, animate, interval=500)
    plt.show()
    t.join()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nEntrando...')