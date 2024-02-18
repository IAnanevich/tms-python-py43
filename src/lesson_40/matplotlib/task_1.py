import matplotlib.pyplot as plt
import numpy as np


time = np.linspace(0, 10, 100)
values_1 = np.sin(time)
values_2 = np.cos(time)

plt.plot(time, values_1, label='Sin')
plt.plot(time, values_2, label='Cos')

plt.xlabel('Время')
plt.ylabel('Значение')
plt.title('График зависимости от времени')
plt.grid()
plt.legend()

plt.show()
