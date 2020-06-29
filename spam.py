from paho.mqtt import client as mqtt

class Client(mqtt.Client):
    def __init__(self, *args, **kwargs):
        super()._init_(*args, **kwargs)



class Publisher(Client):
    def __init__(self, *args, **kwargs):
        super()._init_(*args, **kwargs)


class Subscriber(Client):
    def __init__(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self.on_message = self._class_._on_message
        self.on_subscribe = self._class_._on_subscribe

    def _on_subscribe(self, userdata, mid, granted_qos, properties=None):
        # no puedes hacer esto aqui, estas haciendo un objeto recursivo
        subscriber = Subscriber(client_id)
        # este deberia ser self.connect
        subscriber.connect(broker_ip)
        # lo mismo de la linea anterior
        subscriber.subscribe(topic)
        subscriber.loop_start()
        try:
            while True:
                # para usar sleep tienes que importarlo en la parte de arriba del archivo
                # from time import sleep
                sleep(sleep_time)
        except KeyboardInterrupt:
            # esta instruccion corta el programa
            # si llega aqui el cliente no va acerrar la conexion
            raise
        # self.disconnect
        subscriber.disconnect()
        # self.loop_stop
        subscriber.loop_stop()



    def _on_message(self, userdata, message):
        msg = message.payload.decode("utf8")