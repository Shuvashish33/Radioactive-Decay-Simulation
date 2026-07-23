import numpy as np
import matplotlib.pyplot as plt

# 1. Prepare data
days = np.array([1, 2, 3, 4, 5])
store_1 = np.array([10, 15, 13, 18, 20])
store_2 = np.array([5, 8, 14, 19, 24])

# 2. Draw lines with plt.plot()
plt.plot(days, store_1, label="Downtown Store", color="blue", marker="o")
plt.plot(days, store_2, label="Uptown Store", color="orange", linestyle="--")

# 3. Add axis labels
plt.xlabel("Day of the Week")
plt.ylabel("Sales ($100s)")

# 4. Add the legend box
plt.legend(loc="upper left")

# 5. Display the plot window
plt.show()