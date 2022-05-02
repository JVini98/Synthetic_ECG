import os
import numpy as np
import matplotlib.pyplot as plt

files = os.listdir("./formated_data_AF_filtered")
is_inverted = []

pack = int(input())

upper = 100*pack
lower = (100*pack)-100

files=files[lower : upper]

ecgs = []

for i, file in enumerate(files):
    ecg = np.loadtxt(f"./formated_data_AF_filtered/{file}", dtype=None, delimiter=' ')
    ecg = ecg.T
    ecgs.append(ecg)

plt.figure(figsize=(10, 10))
plt.show()

for i, ecg in enumerate(ecgs):

    plt.figure(figsize=(15, 10))
    plt.plot(ecg)
    plt.title(i)
    plt.show()
    
    anws = str(input())
    if anws=='q':
        break

    if anws == '+': 
        is_inverted.append(1) 
        print(i, True)
    else:
        is_inverted.append(0)
        print(i, False)

    plt.close()
    
file_w = open(f"./is_inverted_{pack}.asc", "w")

for i ,line in enumerate(is_inverted):

    file_w.write(str(line))
    file_w.write("\n")
    file_w.flush()

