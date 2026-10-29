import numpy as np
import matplotlib.pyplot as plt


class Data:
    def __init__(self, xdata, ydata):
        self.xdata = xdata
        self.ydata = ydata

    # Plot the data with labelled axes
    def plot(self):
        plt.plot(self.xdata[1:], self.ydata[1:], 'o')
        plt.xlabel(self.xdata[0])
        plt.ylabel(self.ydata[0])
        plt.show()

    # Return the data values as a Numpy array
    def to_numpy(self, label):
        if label == self.xdata[0]:
            return np.array(self.xdata[1:])
        elif label == self.ydata[0]:
            return np.array(self.ydata[1:])


# Create the free-fall data
falldata = Data(
    ['heights', 1.0, 0.8, 0.6],
    ['times', 0.332, 0.300, 0.251]
)

# Plot the data
falldata.plot()

# Print the heights as a Numpy array
print(falldata.to_numpy('heights'))

# Print the times as a Numpy array
print(falldata.to_numpy('times'))