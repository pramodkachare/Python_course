import matplotlib.pyplot as plt
import numpy as np


x = np.arange(10)

plt.plot(x)
plt.savefig('spider_demo.pdf')
plt.show()

plt.plot(x, 2*x+3)
plt.show()

plt.subplot(2, 2, 1)
plt.plot(x)
plt.subplot(2, 2, 4)
plt.plot(x, 2*x+3)
plt.show()

