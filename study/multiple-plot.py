import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 10., 0.2)

plt.plot(t, t, 'r--',
        t, 2 * t, 'bs',
        t, t**2, 'g^')

plt.title('several graphs')
plt.show()