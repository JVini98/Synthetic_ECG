import os
import numpy as np
import matplotlib.pyplot as plt


out_dir = "/home/jvini/PycharmProjects/TFG_ECG/formated_data_AF_filt_inv"
os.makedirs(out_dir, exist_ok=True)

global_mask = []

for i in range(49):
    mask = np.loadtxt(f'/home/jvini/PycharmProjects/TFG_ECG/inverted_mask/is_inverted_{i+1}.asc', dtype = int, delimiter = ' ')
    global_mask.extend(mask)

global_mask = np.array(global_mask)
print(global_mask)

files = os.listdir("/home/jvini/PycharmProjects/TFG_ECG/formated_data_AF_filtered")

for i, file in enumerate(files):

    ecg = np.loadtxt(f"/home/jvini/PycharmProjects/TFG_ECG/formated_data_AF_filtered/{file}", dtype=None, delimiter=' ')
    f_to_write = open(f'{out_dir}/{file}', "w")

    #if global_mask[i] == 1:
        # plt.plot(ecg.T)
        # plt.title('regular')
        # plt.show()

    ecg = np.round(ecg)

    if global_mask[i] == 1:
        ecg = -ecg
        #plt.plot(ecg.T)
        #plt.title(f'inverted {i}')
        #plt.show()

    for line in ecg:

        f_to_write.write(str(line))
        f_to_write.write("\n")
        f_to_write.flush()