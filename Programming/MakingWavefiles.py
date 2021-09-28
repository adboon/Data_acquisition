# Making the wave files for the experiments
# Files have to be .txt @ 100Hz with the values being Volt amplitudes
# PhD thesis Anna Boon
# 2021 08 31

#%%
import numpy as np
#Parameters to choose
n_st = 5 #number of start up waves before real waves
ratio_s_V = 0.0125 #DUMMY VALUE, NO IDEA WHAT IT ACTUALLY IS (stroke vs volt ratio) [m/V]

#Various parameters which are options
H = np.array([0.004, 0.005, 0.046, 0.09, 0.1, 0.11], dtype=float) #different wave heights [m]
T_ship = np.array([0.32, 0.9, 0.98, 1.4], dtype=float) #different wave periods [s], this is the wave period that you would find if the ship was actually sailing and you were a bystander
U = np.array([0, 0.3, 0.5], dtype=float) # different current velocities [m/s]
t_test = np.array([300, 600, 172800], dtype=float) #different testing times [s]
d = 0.44 #maximum waterdepth [m]
dt = 1/100 #time step (has to be 100 Hz) [s]

#Calculated parameters 
omega = 2*3.141593/T_ship #wave frequency [rad/s]
alpha = (omega**2)*d/9.81 #coefficient to calculate wavenumber
k = (alpha*np.tanh(alpha)**(-0.5))/d #wavenumber [1/m]
labda = 2*3.141593/k #Wavelength [m]
time = np.arange(0,t_test[0],dt) #array of the time [s]
# #%%
# #Checking frequency and everything that the wavemaker needs to preduce to reach what we want in the waves
# #f_wavemaker = f_wave*(c - -U)/c
# c_min = 9.81*np.tanh(k[0]*d)/omega[0]
# c_max = 9.81*np.tanh(k[-1]*d)/omega[-1]
# f_wmaker_min = (1/T_ship[-1])*(c_min + U[-1])/c_min
# f_wmaker_max = (1/T_ship[0])*(c_max + U[-1])/c_max
# T_wmakermin = 1/f_wmaker_max
# T_wmakermax = 1/f_wmaker_min



# %%
#Actually making the files (for all combinations of H, T and U)


for Tw in T_ship:#[0:1]:
    w_ship = 2*3.141593/Tw #omega for this value [rad/s]
    alphaw = (w_ship**2)*d/9.81 #coefficient to calculate wavenumber
    kw = (alphaw*np.tanh(alphaw)**(-0.5))/d #wavenumber [1/m]
    c_s = 9.81*np.tanh(kw*d)/w_ship #propegation velocity of the waves if there was no current [m/s]
    for Uc in U:#[0:1]:
        #Wavemaker and ship model stationary in respect to eachother, so no doppler shift.
        #Only shift because we input the wave frequency without taking velocity into account
        #This means that the only translation that has to be made is f_meas = f_input*(c + U)/c 
        T_wavemaker = Tw*(c_s/(c_s + Uc)) #compensate for that the input T_ship is for the situation of the ship not moving (so no current) [s]
        w = 2*3.141593/T_wavemaker #omega for this value [rad/s]
        if Uc == 0:
            ratio_a_s = 1.36E-04*w**3 - 9.77E-03*w**2 + 2.15E-01*w - 5.07E-01
        if Uc == 0.3:
            ratio_a_s = 6.69E-05*w**3 - 5.67E-03*w**2 + 1.53E-01*w - 3.72E-01
        if Uc == 0.5:
            ratio_a_s =  4.64E-05*w**3 - 4.38E-03*w**2 + 1.32E-01*w - 3.27E-01
        for Hw in H:#[-3:-2]:
            steepness = Hw*(w_ship**2/9.81)/(2*3.141593) #to check if waves are feasible
            stroke_max = 0.5*Hw/ratio_a_s
            if steepness <= (1/15) and stroke_max < 0.125:
                ampl = 0.5*Hw*np.sin(w*time) #all the waveamplitudes
                ramp_nr = int(n_st*Tw/dt) #ramp up and down steps [steps]
                ramp_time = np.arange(0,ramp_nr)
                ampl[0:ramp_nr] = ampl[0:ramp_nr]*ramp_time/ramp_nr#linear ramping [m]
                ampl[-ramp_nr-1:-1] = ampl[-ramp_nr-1:-1]*ramp_time[::-1]/ramp_nr #linear ramping [m]
                stroke = ampl/ratio_a_s #
                volts = stroke/ratio_s_V #volts that will make it happen [V]
            
                file_events = "WaveFiles/reg_wave_"+"H_"+str(Hw)+"T_"+str(Tw)+"U_"+str(Uc)+".txt" #name of file
                f = open(file_events,"w+") #create txt file
                for V in volts:
                    f.write(str(V)) #write data point
                    f.write('\n') #new line
                f.close() #close the file

            ##Plotting the results to check visually
            # import matplotlib.pyplot as plt
            # plt.figure()
            # plt.plot(time[0:1000],volts[0:1000])
            # plt.figure()
            # plt.plot(time[-1000:-1],volts[-1000:-1])








# %%
