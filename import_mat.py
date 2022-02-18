from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np

for i in range(1,8528):

    if i < 10:
        var = f'A0000{i}'
    elif 10 <= i < 100:
        var = f'A000{i}'
    elif 100 <= i < 1000:
        var = f'A00{i}'
    elif 1000 <= i:
        var = f'A0{i}'

    ecg = loadmat(f'training2017/{var}.mat')
    ecg_array = ecg['val'][0]





#plt.figure()
#plt.plot(ecg_array)
#plt.show()