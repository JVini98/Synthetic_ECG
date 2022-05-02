import matplotlib.pyplot as plt
import numpy as np
import ecg_plot

N_subplots = 3

for epochs in (2000,2500):

    fig, axs = plt.subplots(N_subplots,figsize=(16,15))

    for i in range(N_subplots): 
        file_path = "/home/jvini/Escritorio/deepfake-ecg/deepfakeecg/teach_g_each_2/{}_epoch/{}.asc".format(epochs, i)
        ecg = np.loadtxt(file_path, dtype=None, delimiter=' ')
        ecg = ecg.T

        norm = np.linalg.norm(ecg)
        ecg = ecg/norm

        axs[i].plot(ecg)
        axs[i].grid()


    fig.suptitle('{} epoch training'.format(epochs))
    fig.savefig('teach_g_each_2/{}_epoch.png'.format(epochs))
    plt.show()
    