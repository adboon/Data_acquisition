# Check accelerations within wave file
# PhD research Anna Boon
# 30-07-2021

#%%

# files = files that should be checked
# ratio_a_V = ratio between wave amplitude made and volts in the file
# visualize = 1, then it will be visualized
def FindMaxValues(files,ratio_a_V,visualize):
    import numpy as np

    dt = 1/100 #frequentie is 100 Hz

    S = []
    A = []
    V = []
    Eta = []

    for filepath in files:
        f = open(filepath,"r") #create csv file
        amplitude = f.read() #amplitude data
        ampl = amplitude.split()
        f.close() #close the file
        stroke = []
        velocity = []
        acceleration = []
        wave_ampl = []

        for ii in range(2,len(ampl)): #voor alle amplitudes
            eta = float(ampl[ii])*ratio_a_V #wave amplitude [m]
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
            Eta.append(eta)

            stroke.append(stroke_1)
            velocity.append(v1)
            acceleration.append(a)
            wave_ampl.append(eta)


        if visualize == 1:
            import matplotlib.pyplot as plt
            time = np.arange(0,len(ampl)*dt,dt)
            Smax = 0.125
            Vmax = 0.6 
            Amax = 4.6
            Etamax = 0.12 

            plt.figure()
            plt.title(filepath)
            plt.subplot(2,2,1)
            plt.plot(time[0:len(stroke)],stroke)
            plt.plot([time[0],time[len(stroke)]],[Smax, Smax],'--')
            plt.xlabel('Time [s]')
            plt.ylabel('Stroke amplitude [m]')
            plt.legend(['From file','Limit'])

            plt.subplot(2,2,2)
            plt.plot(time[0:len(velocity)],velocity)
            plt.plot([time[0],time[len(velocity)]],[Vmax, Vmax],'--')
            plt.xlabel('Time [s]')
            plt.ylabel('Velocity [m/s]')

            plt.subplot(2,2,3)
            plt.plot(time[0:len(acceleration)],acceleration)
            plt.plot([time[0],time[len(acceleration)]],[Amax, Amax],'--')
            plt.xlabel('Time [s]')
            plt.ylabel('Acceleration [m/s2]')

            plt.subplot(2,2,4)
            plt.plot(time[0:len(wave_ampl)],wave_ampl)
            plt.plot([time[0],time[len(wave_ampl)]],[Etamax, Etamax],'--')
            plt.xlabel('Time [s]')
            plt.ylabel('Wave height [m]')

    max_s = max(S)
    max_v = max(V)
    max_a = max(A)
    max_eta = max(Eta)


    return max_s, max_v, max_a, max_eta






# #%%
# # For specific files to check all
# # t_end = (len(amplitude)-11)/100 #max time
# # T = np.array([0:dt:t_end]) #time array

# file = "02_jonswap_tpk1.15_hs0.04.txt" #name of file
# f = open(file,"r") #create csv file
# amplitude = f.read() #amplitude data
# ampl = amplitude.split()
# f.close() #close the file

# S = []
# A = []
# V = []

# for ii in range(2,len(ampl)): #voor alle amplitudes
#     omega = 2*3.141593/1.15 #wave frequencies [rad/s]
#     ratio_a_s = 2.57*10**(-5)*np.power(omega,3) - 2.75*10**(-3)*np.power(omega,2) + 9.95*10**(-2)*omega - 0.246 #ratio for a current velocity of U = 1 m/s 
#     stroke_1 = float(ampl[ii-2])*ratio_a_V/ratio_a_s #slag [m]
#     stroke_2 = float(ampl[ii-1])*ratio_a_V/ratio_a_s #slag [m]
#     stroke_3 = float(ampl[ii])*ratio_a_V/ratio_a_s #slag [m]
#     v1 = (stroke_1-stroke_2)/(dt) #snelheid [m/s]
#     v2 = (stroke_2-stroke_3)/(dt) #snelheid [m/s]
#     a = (v2-v1)/dt #versnelling [m/s2]
#     S.append(stroke_1)
#     A.append(a)
#     V.append(v1)













# %%
