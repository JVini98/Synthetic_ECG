import matplotlib.pyplot as plt
import numpy as np
import ecg_plot

N_subplots = 3

for epochs in (500,1000,1500,2000):

    fig, axs = plt.subplots(N_subplots,figsize=(16,15))

    for i in range(N_subplots): 
        file_path = "/home/jvini/Escritorio/deepfake-ecg/deepfakeecg/exp_gpu1_out/{}_epoch/{}.asc".format(epochs, i)
        ecg = np.loadtxt(file_path, dtype=None, delimiter=' ')
        ecg = ecg.T

        norm = np.linalg.norm(ecg)
        ecg = ecg/norm

        axs[i].plot(ecg)
        axs[i].grid()


    fig.suptitle('{} epoch training'.format(epochs))
    fig.savefig('{}_epoch.png'.format(epochs))
    plt.show()