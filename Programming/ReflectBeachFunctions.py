# Reflections from beach
# Test script
# Based on: Suh 2001 (Separation of incident.......)
#           Tatavarti 1988 (Incoming and outgoing wave.......)
# To make this work for irregular waves, substitute eta_err (which is now 1 regular wave with noise) with the summation of all the waves within the wave spectrum. 
#%%
#water depth [m], wave steepness [H/lambda], location wave measurements [m], current velocity [m/s], input wave height [m], measured wave elevation [m], time array [s], visualizition (1 = on)
def Reflect_beach(water_depth, steepness, x_loc, U_curr, eta, eta_measured, time, visualization):
    import numpy as np
    import matplotlib.pyplot as plt
    # 'real' parameters
    g = 9.81 #gravitational acceleration [m/s2]
    H = eta*2 #wave height [m]
    lamba = eta*2/steepness #wave length [m]
    k_i =  2*np.pi/lamba #incident wave number [1/m]
    k_r = -k_i #reflected wave number [1/m]
    omega_a = k_i*U_curr + np.sqrt(g*k_i*np.tanh(k_i*water_depth)) #absolute angular frequency [rad/s]
    T_meas = time[-1] #max measuring time [s]

    #Finding the reflection coefficient
    c = np.zeros((4,4))
    F = np.zeros((4,1))
    for kk in range(len(x_loc)):
        #Coefficients according to Suh 2001
        c[0,0] = c[0,0] + (0.5*T_meas + (0.25/omega_a)*(np.sin(2*(omega_a*T_meas - k_i*x_loc[kk])) + np.sin(2*k_i*x_loc[kk])))
        c[0,1] = c[0,1] + 0.5*T_meas*np.cos(k_i*x_loc[kk] + k_r*x_loc[kk]) + (np.sin(2*omega_a*T_meas)/(4*omega_a))*np.cos(k_i*x_loc[kk] - k_r*x_loc[kk]) + ((1-np.cos(2*omega_a*T_meas))/(4*omega_a))*np.sin(k_i*x_loc[kk] - k_r*x_loc[kk])
        c[0,2] = c[0,2] + (0.25/omega_a)*(np.cos(2*(omega_a*T_meas - k_i*x_loc[kk]))+np.cos(2*k_i*x_loc[kk]))
        c[0,3] = c[0,3] + -0.5*T_meas*np.sin(k_i*x_loc[kk] + k_r*x_loc[kk]) - (np.sin(2*omega_a*T_meas)/(4*omega_a))*np.sin(k_i*x_loc[kk] - k_r*x_loc[kk]) - ((1-np.cos(2*omega_a*T_meas))/(4*omega_a))*np.cos(k_i*x_loc[kk] - k_r*x_loc[kk])
        c[1,1] = c[1,1] + 0.5*T_meas + (0.25/omega_a)*(np.sin(2*(omega_a*T_meas + k_r*x_loc[kk]))-np.sin(2*k_r*x_loc[kk]))
        c[1,2] = c[1,2] + -0.5*T_meas*np.sin(k_i*x_loc[kk] + k_r*x_loc[kk]) - (np.sin(2*omega_a*T_meas)/(4*omega_a))*np.sin(k_i*x_loc[kk] - k_r*x_loc[kk]) + ((1-np.cos(2*omega_a*T_meas))/(4*omega_a))*np.cos(k_i*x_loc[kk] - k_r*x_loc[kk])
        c[1,3] = c[1,3] + (0.25/omega_a)*(np.cos(2*(omega_a*T_meas + k_r*x_loc[kk]))-np.cos(2*k_r*x_loc[kk]))
        c[2,2] = c[2,2] + 0.5*T_meas - (0.25/omega_a)*(np.sin(2*(omega_a*T_meas - k_i*x_loc[kk]))) + np.sin(2*k_i*x_loc[kk])
        c[2,3] = c[2,3] + -0.5*T_meas*np.cos(k_i*x_loc[kk] + k_r*x_loc[kk]) + (np.sin(2*omega_a*T_meas)/(4*omega_a))*np.cos(k_i*x_loc[kk] - k_r*x_loc[kk]) + ((1-np.cos(2*omega_a*T_meas))/(4*omega_a))*np.sin(k_i*x_loc[kk] - k_r*x_loc[kk])
        c[3,3] = c[3,3] + 0.5*T_meas - (0.25/omega_a)*(np.sin(2*(omega_a*T_meas+k_r*x_loc[kk])) - np.sin(2*k_r*x_loc[kk]))
        F[0] = F[0] + np.trapz( np.cos(omega_a*time - k_i*x_loc[kk])*eta_measured[:,kk], x=time)
        F[1] = F[1] + np.trapz( np.cos(omega_a*time + k_r*x_loc[kk])*eta_measured[:,kk], x=time)
        F[2] = F[2] + np.trapz( np.sin(omega_a*time - k_i*x_loc[kk])*eta_measured[:,kk], x=time)
        F[3] = F[3] + np.trapz(-np.sin(omega_a*time + k_r*x_loc[kk])*eta_measured[:,kk], x=time)
    c[1,0] = c[0,1]
    c[2,0] = c[0,2]
    c[3,0] = c[0,3]
    c[2,1] = c[1,2]
    c[3,1] = c[1,3]
    c[3,2] = c[2,3]

    #find solutions using least squares
    from scipy.optimize import leastsq

    X = np.linalg.lstsq(c, F,rcond=None)[0]

    phi_i_result = np.arctan(X[2]/X[0]) #incident phase angle [rad]
    phi_r_result = np.arctan(X[3]/X[1]) #reflected phase angle [rad]    
    H_i = (2*(X[0] + X[2])/(np.cos(phi_i_result)+np.sin(phi_i_result))) #incident wave height [m]
    H_r = (2*(X[1] + X[3])/(np.cos(phi_r_result)+np.sin(phi_r_result))) #reflected wave height [m]
    kr = H_r/H_i #Found reflection coefficient [-]

    if visualization == 1:
    # Visualization
        for jj in range(1,len(x_loc)):
            eta_X = X[0]*np.cos(omega_a*time - k_i*x_loc[jj]) + X[1]*np.cos(omega_a*time + k_r*x_loc[jj]) + X[2]*np.sin(omega_a*time - k_i*x_loc[jj]) - X[3]*np.sin(omega_a*time + k_r*x_loc[jj])
            eta_found = H_i*0.5*np.cos(-omega_a*time + k_i*x_loc[jj] + phi_i_result) + H_r*0.5*np.cos(omega_a*time + k_r*x_loc[jj] + phi_r_result)
            plt.figure(jj)
            plt.title(['Location =',x_loc[jj],'m'])
            plt.plot(time,eta_measured[:,jj])
            plt.plot(time,eta_X)
            plt.plot(time,eta_found)
            plt.legend(['Measured', 'X', 'Found'], loc='upper left')

    return kr, H_i, H_r

# k_refl, H_incident, H_reflected =  Reflect_beach(water_depth, steepness, x_loc, U_curr, amp_wave, eta_measured, time, 1)

#     # 'real' parameters
# water_depth = 0.5 #water depth [m]
# steepness = 0.03 #wave steepness [-]
# x_loc = [0.1, 0.2, 0.4, 0.9] #locations wave measurements [m]
# kr_calc = 0.1 #reflection coefficient with which the waves are calculated [-]
# e_noise_amp = 0.01#.5 #amplification of the noise
# phi_i = 0*np.pi #phase difference incoming wave [rad]
# phi_r = 0.01*np.pi #phase difference reflected wave [rad]
# dt = 0.05 #time stepsize [s]
# T_meas = 10 #length of time measured [s]
# U_curr = 0 #current velocity [m/s]
# eta = 0.015 #wave amplitude [m]

# H = eta*2 #wave height [m]
# lamba = eta*2/steepness #wave length [m]
# k_i =  2*np.pi/lamba #incident wave number [1/m]
# k_r = -k_i #reflected wave number [1/m]
# omega_a = k_i*U_curr + np.sqrt(g*k_i*np.tanh(k_i*water_depth)) #absolute angular frequency [rad/s]
# t = np.arange(0,T_meas+dt,dt) #runtime [s]
# Hr = H*kr_calc #expected reflected wave height [m]
# omega_r = omega_a - k_i*U_curr #angular frequency in moving frame of reference

# ##Not necessary for this part
# ## for incident waves k = k_i and U = U, for reflected waves k = k_r and U = -U
# #H0 = H*(2*k0*(U + (omega_r/(2*k))*(1+(2*k*h/(np.sinh(2*k*h)))))/(omega_r*(1+2*k0*h/np.sinh(2*k0*h)))) #wave heights in zero-current area [m]
# #C_gr = 0.5*(omega_r/k)*(1+2*k*h/sinh(2*k*h)) #group velocity wavevs [m/s]
# ##dependences: S(omega_a,U), S(omega_a)
# ##they look at the transformation of a spectrum when the waves move from an area without current to an area with current
# #S0 = S*(2*k0*(U+(omega_r/2*k)*(1+2*k*h/sinh(2*k*h))))/(omega_r*(1+2*k0*h/sinh(2*k0*h))) #spectral density of free-surface displacement in quiescent area (S0) related to that in current area (S)

# eta = np.zeros((len(t),len(x_loc)))
# eta_measured = np.zeros((len(t),len(x_loc)))
# for jj in range(len(x_loc)):
#     eta[:,jj] = eta*np.cos(-omega_a*t + k_i*x_loc[jj] + phi_i) + 0.5*Hr*np.cos(omega_a*t + k_r*x_loc[jj] + phi_r) #measured wave height [m] location 4
#     eta_measured[:,jj] = (eta[:,jj] + (np.random.rand(len(t))-0.5)*e_noise_amp) #measured wave height with error [m] location 4

# %%
