import matplotlib.pyplot as plt
import numpy as np

categories = ['Cat1', 'Cat2', 'Cat3']
values = [20, 55, 25]

plt.barh(categories, values, color=['green', 'blue', 'red'])

plt.xlabel('Values')
plt.ylabel('Categories')
plt.title('Гистограмма')
plt.grid()

plt.show()
