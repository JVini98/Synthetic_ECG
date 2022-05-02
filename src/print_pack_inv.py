import os
import numpy as np
import matplotlib.pyplot as plt

print("what pack?")
pack = int(input())

files = os.listdir("/home/jvini/PycharmProjects/TFG_ECG/formated_data_AF_filtered")
mask = np.loadtxt(f'/home/jvini/PycharmProjects/TFG_ECG/is_inverted_{pack}.asc', dtype = int, delimiter = ' ')

upper = 100*pack
lower = (100*pack)-100

files=files[lower : upper]
ecgs = []

for i, file in enumerate(files):
    ecg = np.loadtxt(f"/home/jvini/PycharmProjects/TFG_ECG/formated_data_AF_filtered/{file}", dtype=None, delimiter=' ')
    ecg = ecg.T
    ecgs.append(ecg)

plt.figure(figsize=(15, 10))

for ecg in ecgs:
    plt.plot(ecg)

plt.show()

plt.figure(figsize=(15, 10))

for i,ecg in enumerate(ecgs):
    if mask[i] == 1:
        ecgs[i] = -ecg
    plt.plot(ecgs[i])

plt.show()