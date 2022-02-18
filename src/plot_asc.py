import numpy as np


file_path = '/home/jvini/Escritorio/deepfake-ecg/0.asc'
ecg = np.loadtxt(file_path)
print(ecg)