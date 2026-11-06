import matplotlib.pyplot as plt
from collections import deque
import matplotlib.animation as animation
import math
import serial

PORT = '/dev/cu.usbmodem3377327732371'
BAUD = 115200
ser = None
try:
    ser = serial.Serial(PORT, BAUD, timeout=0.02)

    fig, ax = plt.subplots()
    line = ax.plot([], [])[0]
    ax.set_ylim(-1100, 1100)

    x_data = deque(maxlen=500)
    y_data = deque(maxlen=500)

    def update(frame):
        try:
            while ser.in_waiting > 0:
                raw_text = ser.readline()
                try:
                    string = raw_text.decode('utf-8')
                    clean_string = string.strip()
                    clean_parts = clean_string.split(",")
                    t = int(clean_parts[0])
                    value = int(clean_parts[1])
                    x_data.append(t)
                    y_data.append(value)
                except (ValueError, IndexError):
                    pass
        except OSError:
            print("the board has been disconnected")
            ani.pause()
            return line,
        line.set_data(x_data, y_data)
        if x_data:
            ax.set_xlim(x_data[0], x_data[-1])
        return line,

    ani = animation.FuncAnimation(fig, update, interval=50) 

    plt.show()
except serial.SerialException:
    print("board is unplugged, check board")
finally:
    if ser is not None:
        ser.close()
        