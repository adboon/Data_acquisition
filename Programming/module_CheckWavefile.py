# Check accelerations within wave file
# PhD research Anna Boon
# 30-07-2021

#%%

# files = files that should be checked
# ratio_a_V = ratio between wave amplitude made and volts in the file
# Peak period of the waves [s]
# Current velocity [m/s]
# visualize = 1, then it will be visualized
def FindMaxValues(files,Tp,Uc,ratio_s_V,visualize):
    import numpy as np

    dt = 1/100 #frequentie is 100 Hz

    S = []
    V = []
    A = []
    Eta = []

    for filepath in files:
        f = open(filepath,"r") #create csv file
        amplitude = f.read() #amplitude data
        ampl = amplitude.split()
        ampl.insert(0,0)
        ampl.insert(-1,0)
        ampl = np.array(ampl,dtype=float) #convert to list of floats
        f.close() #close the file

        omega = 2*3.141593/Tp #wave frequencies [rad/s]
        if Uc <= 0.15:
            ratio_a_s = 1.36E-04*omega**3 - 9.77E-03*omega**2 + 2.15E-01*omega - 5.07E-01
        elif Uc <= 0.4:
            ratio_a_s = 6.69E-05*omega**3 - 5.67E-03*omega**2 + 1.53E-01*omega - 3.72E-01
        elif Uc <= 0.6:
            ratio_a_s =  4.64E-05*omega**3 - 4.38E-03*omega**2 + 1.32E-01*omega - 3.27E-01
        else:    
            ratio_a_s = 2.57*10**(-5)*np.power(omega,3) - 2.75*10**(-3)*np.power(omega,2) + 9.95*10**(-2)*omega - 0.246 #ratio for a current velocity of U = 1 m/s 
        stroke = ampl*ratio_s_V #slag [m]
        velocity = (stroke[0:-3]-stroke[1:-2])/(dt) #snelheid [m/s]
        v2 = (stroke[1:-2]-stroke[2:-1])/(dt) #snelheid [m/s]
        acceleration = (v2-velocity)/dt #versnelling [m/s2]
        eta = stroke*ratio_a_s #from stroke to wave amplitude 
        
        S.insert(-1,stroke[1:-2])
        V.insert(-1,velocity[1:-2])
        A.insert(-1,acceleration[1:-2])
        Eta.insert(-1,eta[1:-2])

        if visualize == 1:
            import matplotlib.pyplot as plt
            time = np.arange(0,len(ampl)*dt,dt)
            Smax = 0.1 #UNTIL LONGER GUIDESS ARE PLACED, OTHERWISE 0.125 #Max length of the wedge
            Vmax = 0.6 #Max of the motor
            Amax = 4.6 #Max of the motor
            Etamax = 0.12 #Height of the sides of the tank
            Etamin = 0.005 #Capillary limit

            plt.figure()
            plt.subplot(2,2,1)
            plt.plot(time[0:len(stroke[1:-2])],stroke[1:-2])
            plt.plot([time[0],time[-1]],[Smax, Smax],'--')
            plt.legend(['From file','Maxima'],loc='lower right')
            plt.xlabel('Time [s]')
            plt.ylabel('Stroke amplitude [m]')

            plt.subplot(2,2,2)
            plt.plot(time[0:len(velocity[1:-2])],velocity[1:-2])
            plt.plot([time[0],time[-1]],[Vmax, Vmax],'--')
            plt.xlabel('Time [s]')
            plt.ylabel('Velocity [m/s]')

            plt.subplot(2,2,3)
            plt.plot(time[0:len(acceleration[1:-2])],acceleration[1:-2])
            plt.plot([time[0],time[-1]],[Amax, Amax],'--')
            plt.xlabel('Time [s]')
            plt.ylabel('Acceleration [m/s2]')

            plt.subplot(2,2,4)
            plt.plot(time[0:len(eta[1:-2])],eta[1:-2])
            plt.plot([time[0],time[-1]],[Etamax, Etamax],'--')
            #plt.plot([time[0],time[-1]],[Etamin, Etamin],'.-') Already taken care of when wavefiles are made
            plt.xlabel('Time [s]')
            plt.ylabel('Wave height [m]')
            plt.suptitle('...'+filepath[-40:])



    S = np.array(S)
    V = np.array(V)
    A = np.array(A)
    Eta = np.array(Eta)
    max_s = max(S.flatten())
    max_v = max(V.flatten())
    max_a = max(A.flatten())
    max_eta = max(Eta.flatten())
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
