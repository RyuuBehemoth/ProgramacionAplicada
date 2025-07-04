import serial
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from math import radians
from collections import deque
import time
import numpy as np

# Configuración del puerto
puerto = 'COM3'
baudrate = 9600

# Conectar al ESP32
try:
    ser = serial.Serial(puerto, baudrate, timeout=1)
    print(f"✅ Conectado a {puerto}")
    time.sleep(2)
except Exception as e:
    print(f"❌ No se pudo abrir {puerto}: {e}")
    exit()

# Parámetros del radar
MAX_PUNTOS = 60  # historial para desvanecimiento
trail = deque(maxlen=MAX_PUNTOS)

# Crear la figura
plt.ion()
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, polar=True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.set_thetamin(0)
ax.set_thetamax(180)
ax.set_rlim(0, 200)

scatter = None  # inicialización

try:
    while True:
        linea = ser.readline().decode('utf-8').strip()

        if "," in linea:
            try:
                linea = linea.replace(".", "")
                ang_str, dist_str = linea.split(',')
                ang = int(ang_str)
                dist = int(dist_str)

                if 0 <= ang <= 180 and 2 <= dist <= 400:
                    rad = radians(ang)
                    trail.append((rad, dist))

                    # Preparar datos y colores
                    thetas, rs = zip(*trail)
                    alphas = np.linspace(0.2, 1, len(trail))  # más nuevo = más opaco
                    colors = [(0, 1, 0, a) for a in alphas]

                    # Limpiar solo lo necesario
                    ax.clear()
                    ax.set_theta_zero_location("N")
                    ax.set_theta_direction(-1)
                    ax.set_thetamin(0)
                    ax.set_thetamax(180)
                    ax.set_rlim(0, 200)
                    ax.set_title("Radar ESP32 en Tiempo Real", va='bottom')

                    for i in range(len(thetas)):
                        ax.plot(thetas[i], rs[i], 'o', color=colors[i])

                    plt.pause(0.001)
            except Exception as e:
                print(f"⚠️ Error procesando línea: {linea} → {e}")

except KeyboardInterrupt:
    print("\n🛑 Lectura detenida por el usuario.")
finally:
    ser.close()
    plt.ioff()
    plt.show()
