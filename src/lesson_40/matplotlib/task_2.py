import matplotlib.pyplot as plt
import numpy as np

x_data = np.random.rand(50)
y_data = np.random.rand(50)

plt.scatter(x_data, y_data, c='red', label='Данные')

plt.annotate('Интересная точка', xy=(0.2, 0.6), xytext=(0.5, 0.8))

plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('Диаграмма рассеяния')
plt.grid()
plt.legend()

plt.show()
