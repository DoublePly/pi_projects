from matplotlib import pyplot as plt
import numpy as np

temp = []

file = open('weather.txt', 'r')

for line in file.read().splitlines():
    if line:
        temp.append(float(line))
file.close()


ypoints = np.array(temp)
print(temp)
plt.plot(ypoints)
plt.show()