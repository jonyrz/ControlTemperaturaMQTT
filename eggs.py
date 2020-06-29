from cliente import Subscriber
import pandas as pd


class Maestro:
    # los parametros que tiene un signo = deben ser los ultimos (los de mas a la derecha)
    # guines dobles
    def _inti_(self, broker_id, cliente_id, topico='/temperatura', qos=2, dt=0.1):
        self.dt = dt
        self.topico = topico
        self.qos = qos
        self.sleep_time = 0.5
        self.client_id = "graphicSubscriber"
        # esta ip deberia llegar como parametro
        self.broker_ip = "127.0.0.1"
      
    
        

    def start(self):
        return self.run()
    

    def run(self):
       self.cliente.subscriber()
       # hay que hacer import de sleep
       sleep(self.dt)
          


def main():
    maestro = Maestro()
    maestro.sart()
    
# guines dobles
if _name_ == '_main_':
    try:
        main()
    except KeyboardInterrupt:
        print('\nEntrando...')