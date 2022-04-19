from scipy.io import loadmat
import pandas as pd
import os
import shutil
import matplotlib.pyplot as plt
import numpy as np

out_dir = "/home/jvini/PycharmProjects/TFG_ECG/formated_data_AF"
os.makedirs(out_dir, exist_ok=True)

df = pd.read_csv(r'/home/jvini/PycharmProjects/TFG_ECG/training2017/REFERENCE-original.csv')
categories = df.values

af_files_counter = 1

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

        if 5000 <= ecg_array.size < 10000:

            file = open(f'{out_dir}/{10001 + af_files_counter*10}.asc', "a")

            for i ,line in enumerate(ecg_array):

                if i == 5000: break

                file.write(str(line))
                file.write("\n")
                file.flush()

            shutil.copy(f'{out_dir}/{10001 + af_files_counter * 10}.asc',
                        f'{out_dir}/{10002 + af_files_counter * 10}.asc')
            shutil.copy(f'{out_dir}/{10001 + af_files_counter * 10}.asc',
                        f'{out_dir}/{10003 + af_files_counter * 10}.asc')
            shutil.copy(f'{out_dir}/{10001 + af_files_counter * 10}.asc',
                        f'{out_dir}/{10004 + af_files_counter * 10}.asc')
            shutil.copy(f'{out_dir}/{10001 + af_files_counter * 10}.asc',
                        f'{out_dir}/{10005 + af_files_counter * 10}.asc')

            af_files_counter = af_files_counter + 1
            





#plt.figure()
#plt.plot(ecg_array)
#plt.show()