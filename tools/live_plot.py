import matplotlib.pyplot as plt
from collections import deque
import matplotlib.animation as animation
import math

fig, ax = plt.subplots()
line = ax.plot([], [])[0]
ax.set_ylim(-1.1, 1.1)


x_data = deque(maxlen=500)
y_data = deque(maxlen=500)

def update(frame):
    x_data.append(frame)
    y_data.append(math.sin(frame/10))
    line.set_data(x_data, y_data)
    ax.set_xlim(x_data[0], x_data[-1])
    return (line, )

ani = animation.FuncAnimation(fig, update, interval=50) 


plt.show()

