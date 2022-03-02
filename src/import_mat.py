from scipy.io import loadmat
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

out_dir = "/home/jvini/PycharmProjects/TFG_ECG/formated_data_AF"
os.makedirs(out_dir, exist_ok=True)

df = pd.read_csv(r'/home/jvini/PycharmProjects/TFG_ECG/training2017/REFERENCE-original.csv')
categories = df.values

for i in range(1, 8528):

    if categories.item((i-1, 1)) == 'A':
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

        file = open(f'{out_dir}/{i}.asc', "a")

        for line in ecg_array:
            file.write(str(line))
            file.write("\n")
            file.flush()





#plt.figure()
#plt.plot(ecg_array)
#plt.show()