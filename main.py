import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
path = r"C:\Users\Riade\Documents\instruments\benchmarkneutrons_0.01_to_3_100values_inc"

i = 0
depths, intensities = [], []
while True:
    try:
        f = open(path + "\\" + str(i) + "\\mon.dat", "r")
        lines = f.readlines()
        depth_par = float(lines[9].split("=")[-1][:-1])
        intensity_par = float(lines[19].split("; Mean")[-0].split("Max=")[-1])
        depths.append(depth_par)
        intensities.append(intensity_par)
        i += 1
    except OSError:
        break
plt.xlabel("Sample depth")
plt.ylabel("Intensity")
log_intensities = np.log(intensities)
#plt.plot(depths, intensities)
plt.plot(depths, log_intensities)
plt.show()

model = LinearRegression().fit(np.array(depths).reshape(-1, 1), log_intensities)
print(model.coef_,model.intercept_)

