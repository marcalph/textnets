import matplotlib.pyplot as plt  # type: ignore

import numpy as np  # type: ignore

x = np.linspace(0, 20, 100)
# Create a list of evenly-spaced numbers over the range
newvariable896 = np.sin(x)
plt.plot(x, newvariable896)
# Plot the sine of each x point
plt.show()
