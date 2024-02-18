import matplotlib.pyplot as plt
import numpy as np

grades = np.random.randint(1, 11, 100)

plt.hist(grades, bins=10, color='green', alpha=0.7)

plt.xlabel('Оценки')
plt.ylabel('Студенты')
plt.title('Гистограмма')
plt.grid()
plt.legend()

plt.show()
