import matplotlib.pyplot as plt
import numpy as np
import ecg_plot

file_path = '/home/jvini/Escritorio/deepfake-ecg/0.asc'
ecg = np.loadtxt(file_path, dtype=None, delimiter=' ')
ecg = ecg.T

norm = np.linalg.norm(ecg)
ecg = ecg/norm

fig, axs = plt.subplots(8)

for i in range(8):
    axs[i].plot(ecg[i])

plt.savefig('represented_ecg.png', dpi=300)
plt.show()