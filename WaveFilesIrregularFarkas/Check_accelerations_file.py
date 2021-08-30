# Check accelerations within wave file
# PhD research Anna Boon
# 30-07-2021

#%%
import numpy as np
import glob
files = glob.glob("/home/anna/Documents/1Work_in_progress/WaveFilesIrregularFarkas/*.txt") #find all tdms files in a certain folder
files.sort()


ratio_a_V = 0.0422 #4.22 mm/volt (should check with Farkas)
dt = 1/100 #frequentie is 100 Hz


S = []
A = []
V = []

for filepath in files[0:4]:
    f = open(filepath,"r") #create csv file
    amplitude = f.read() #amplitude data
    ampl = amplitude.split()
    f.close() #close the file

    for ii in range(2,len(ampl)): #voor alle amplitudes
        omega = 2*3.141593/1.15 #wave frequencies [rad/s]
        ratio_a_s = 2.57*10**(-5)*np.power(omega,3) - 2.75*10**(-3)*np.power(omega,2) + 9.95*10**(-2)*omega - 0.246 #ratio for a current velocity of U = 1 m/s 
        stroke_1 = float(ampl[ii-2])*ratio_a_V/ratio_a_s #slag [m]
        stroke_2 = float(ampl[ii-1])*ratio_a_V/ratio_a_s #slag [m]
        stroke_3 = float(ampl[ii])*ratio_a_V/ratio_a_s #slag [m]
        v1 = (stroke_1-stroke_2)/(dt) #snelheid [m/s]
        v2 = (stroke_2-stroke_3)/(dt) #snelheid [m/s]
        a = (v2-v1)/dt #versnelling [m/s2]
        S.append(stroke_1)
        A.append(a)
        V.append(v1)

max_s = max(S)
max_v = max(V)
max_a = max(A)


#%%
# For specific files to check all
# t_end = (len(amplitude)-11)/100 #max time
# T = np.array([0:dt:t_end]) #time array

file = "02_jonswap_tpk1.15_hs0.04.txt" #name of file
f = open(file,"r") #create csv file
amplitude = f.read() #amplitude data
ampl = amplitude.split()
f.close() #close the file

S = []
A = []
V = []

for ii in range(2,len(ampl)): #voor alle amplitudes
    omega = 2*3.141593/1.15 #wave frequencies [rad/s]
    ratio_a_s = 2.57*10**(-5)*np.power(omega,3) - 2.75*10**(-3)*np.power(omega,2) + 9.95*10**(-2)*omega - 0.246 #ratio for a current velocity of U = 1 m/s 
    stroke_1 = float(ampl[ii-2])*ratio_a_V/ratio_a_s #slag [m]
    stroke_2 = float(ampl[ii-1])*ratio_a_V/ratio_a_s #slag [m]
    stroke_3 = float(ampl[ii])*ratio_a_V/ratio_a_s #slag [m]
    v1 = (stroke_1-stroke_2)/(dt) #snelheid [m/s]
    v2 = (stroke_2-stroke_3)/(dt) #snelheid [m/s]
    a = (v2-v1)/dt #versnelling [m/s2]
    S.append(stroke_1)
    A.append(a)
    V.append(v1)


import matplotlib.pyplot as plt

plt.figure()
plt.plot(S)
plt.xlabel('Time [s]')
plt.ylabel('Stroke amplitude [m]')

plt.figure()
plt.plot(V)
plt.xlabel('Time [s]')
plt.ylabel('Velocity [m/s]')

plt.figure()
plt.plot(A)
plt.xlabel('Time [s]')
plt.ylabel('Acceleration [m/s2]')












# %%
