# Reading in TDMS files in Python
# PhD project Anna Boon
# 2021 07 19

#%%
import module_TDMSfile
import module_FindingEvents
import module_ReflectionsBeach
from imp import reload
import numpy as np
reload(module_FindingEvents)
reload(module_TDMSfile)
reload(module_ReflectionsBeach)
from module_FindingEvents import *
from module_TDMSfile import *
from module_ReflectionsBeach import *


filepath = "/home/anna/Documents/1Work_in_progress/Programming/_NAME_2021_07_19_16_59_12.tdms"
# filepath = "davs://adbo@nextcloud.dragundo.net/remote.php/webdav/Documents/PhD/3Programming/LabVIEW/DataTest/_NAME_2021_07_19_16_59_12.tdms" #Path to file and filename

group_name, properties, Name, Data, time = readingTDMSfile(filepath)

plottingTDMSfile(filepath,850) #filepath, resolution (steps that are plotted (1 = every step, 100 = every 100 steps))


folder = "/home/anna/Documents/1Work_in_progress/Programming/*.tdms"
cut_off = 1.2 #DUMMY VALUE AND CALC SHOULD BE CHANGED
Finding_events(folder, cut_off , 1)




# %%
#Code to work with the module_ReflectionsBeach


g = 9.81 #gravitational acceleration [m/s2]
water_depth = 0.5 #water depth [m]
steepness = 0.03 #wave steepness [-]
x_loc = [0.1, 0.2, 0.4, 0.9] #locations wave measurements [m]
kr_calc = 0.1 #reflection coefficient with which the waves are calculated [-]
e_noise_amp = 0.01#.5 #amplification of the noise
phi_i = 0*np.pi #phase difference incoming wave [rad]
phi_r = 0.01*np.pi #phase difference reflected wave [rad]
dt = 0.05 #time stepsize [s]
T_meas = 10 #length of time measured [s]
U_curr = 0 #current velocity [m/s]
amp_wave = 0.015 #wave amplitude [m]
time = np.arange(0,T_meas+dt,dt) #runtime [s]

H = amp_wave*2 #wave height [m]
lamba = amp_wave*2/steepness #wave length [m]
k_i =  2*np.pi/lamba #incident wave number [1/m]
k_r = -k_i #reflected wave number [1/m]
omega_a = k_i*U_curr + np.sqrt(g*k_i*np.tanh(k_i*water_depth)) #absolute angular frequency [rad/s]
t = np.arange(0,T_meas+dt,dt) #runtime [s]
Hr = H*kr_calc #expected reflected wave height [m]
omega_r = omega_a - k_i*U_curr #angular frequency in moving frame of reference

##Not necessary for this part
## for incident waves k = k_i and U = U, for reflected waves k = k_r and U = -U
#H0 = H*(2*k0*(U + (omega_r/(2*k))*(1+(2*k*h/(np.sinh(2*k*h)))))/(omega_r*(1+2*k0*h/np.sinh(2*k0*h)))) #wave heights in zero-current area [m]
#C_gr = 0.5*(omega_r/k)*(1+2*k*h/sinh(2*k*h)) #group velocity wavevs [m/s]
##dependences: S(omega_a,U), S(omega_a)
##they look at the transformation of a spectrum when the waves move from an area without current to an area with current
#S0 = S*(2*k0*(U+(omega_r/2*k)*(1+2*k*h/sinh(2*k*h))))/(omega_r*(1+2*k0*h/sinh(2*k0*h))) #spectral density of free-surface displacement in quiescent area (S0) related to that in current area (S)

eta = np.zeros((len(t),len(x_loc)))
eta_measured = np.zeros((len(t),len(x_loc)))
for jj in range(len(x_loc)):
    eta[:,jj] = amp_wave*np.cos(-omega_a*t + k_i*x_loc[jj] + phi_i) + 0.5*Hr*np.cos(omega_a*t + k_r*x_loc[jj] + phi_r) #measured wave height [m] location 4
    eta_measured[:,jj] = (eta[:,jj] + (np.random.rand(len(t))-0.5)*e_noise_amp) #measured wave height with error [m] location 4


from module_ReflectionsBeach import *
#For irregular waves: go through the function with each wave
#water depth [m], wave steepness [H/lambda], location wave measurements [m], current velocity [m/s], input wave height [m], measured wave elevation [m], time array [s], visualizition (1 = on)
k_refl, H_incident, H_reflected =  Reflect_beach(water_depth, steepness, x_loc, U_curr, amp_wave, eta_measured, time, 1)