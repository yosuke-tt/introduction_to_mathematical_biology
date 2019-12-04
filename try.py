import numpy as np
import matplotlib.pyplot as plt


a = np.arange( 0, 1, 0.01 )
y = 2 * a

print(a.shape)
print(y.shape)

plt.plot( a, y )
plt.show()
