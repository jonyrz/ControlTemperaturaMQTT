#es ejemplo con leector de serial
import subscriptor
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import re
import threading

gData = []
gData.append([0])
gData.append([0])
#Configuramos la gráfica
fig = plt.figure()
ax = fig.add_subplot(111)
hl, = plt.plot(gData[0], gData[1])
plt.ylim(-90, 90)
plt.xlim(0,200)
#

def GetData(out_data):
    # with serial.Serial('/dev/ttyUSB1',115200, timeout=1) as fd:
    with open("datos.csv") as fd:
        #print(ser.isOpen())
        fd.readline()
        while True:
            line = fd.readline()
            try:
                # out_data[1].append( float(res.group(1)) )
                out_data[1].append(float(line))
                if len(out_data[1]) > 200:
                    out_data[1].pop(0)
            except:
                pass

def update_line(num, hl, data):
    hl.set_data(range(len(data[1])), data[1])
    return hl,
# Configuramos la función que "animará" nuestra gráfica
line_ani = animation.FuncAnimation(fig, update_line, fargs=(hl, gData),
                                    interval=50, blit=False)

dataCollector = threading.Thread(target = GetData, args=(gData,))
dataCollector.start()
plt.show()
dataCollector.join()
