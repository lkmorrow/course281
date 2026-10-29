import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the two data files
decay1 = pd.read_excel('decay1.xlsx')
decay2 = pd.read_excel('decay2.xlsx')

# Get time and counts from the first two columns
t1 = decay1.iloc[:, 0].to_numpy()
N1 = decay1.iloc[:, 1].to_numpy()

t2 = decay2.iloc[:, 0].to_numpy()
N2 = decay2.iloc[:, 1].to_numpy()

# Calculate the uncertainties
sigma1 = np.sqrt(N1)
sigma2 = np.sqrt(N2)

# Create one window containing three graphs
fig, ax = plt.subplots(3, 1, figsize=(6, 9))

# Graph 1: Original data
ax[0].plot(t1, N1, 'o', label='Decay 1')
ax[0].plot(t2, N2, 'o', label='Decay 2')
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Counts per minute')
ax[0].set_title('Radioactive decay data')
ax[0].legend()

# Graph 2: Data with error bars
ax[1].errorbar(t1, N1, yerr=sigma1, fmt='o', label='Decay 1')
ax[1].errorbar(t2, N2, yerr=sigma2, fmt='o', label='Decay 2')
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Counts per minute')
ax[1].set_title('Radioactive decay with uncertainties')
ax[1].legend()

# Graph 3: Data with error bars and logarithmic y-axis
ax[2].errorbar(t1, N1, yerr=sigma1, fmt='o', label='Decay 1')
ax[2].errorbar(t2, N2, yerr=sigma2, fmt='o', label='Decay 2')
ax[2].set_yscale('log')
ax[2].set_xlabel('Time')
ax[2].set_ylabel('Counts per minute (log scale)')
ax[2].set_title('Radioactive decay on a logarithmic scale')
ax[2].legend()

# Adjust spacing and show all graphs together
plt.tight_layout()
plt.show()

"""(i) The error bars appear bigger relative to the plotted values
near the end because the counts are smaller there. The relative uncertainty
increases as the count decreases.

(ii) The plots look approximately like straight lines because exponential
decay becomes linear on a logarithmic scale. Near the end, the constant background
B becomes important, so the total count no longer behaves like a pure exponential."""
