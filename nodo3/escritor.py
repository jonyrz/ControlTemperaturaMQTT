from datetime import datetime
import csv


class Escritor:
    def __init__(self):
        self.f = open("datos.csv", "w")
        self.csv = csv.writer(self.f)

    def escribir(self, temepratura, ventilador):
        fecha = datetime.now()
        registro = (fecha.isoformat(" "), "{:.2f}".format(temepratura), ventilador)
        self.csv.writerow(registro)

    def close(self):
        self.f.close()
