#Calculations of irregular waves
#PhD Anna Boon
#2021 08 31

#%%
#Calculations from Ocean Waves Exercise3, wave_spectrum
def SpectrumData(eta,visual):
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.fft import fft, fftfreq
    from scipy import signal


    dt = 1/100 # 100Hz
    Fs = 1/dt #Sampling rate [Hz]
    N = len(eta) #Number of samples
    d_f = Fs/N #Stepsize frequency [Hz]
    f = np.arange(d_f,Fs//2,d_f) #Frequencies [Hz]
    fId = np.arange(1,len(f)) 

    fft_eta = fft(eta) #FFT the data
    freq = fftfreq(N,d_f)#[:N//2]
    # fft_eta = fft_eta[fId,:] #Only one side needed
    A = 2/N*np.real(fft_eta)
    B = 2/N*np.imag(fft_eta)
    E = (A**2 + B**2)/2 #E(i,b) = ai^2/2 = variance at frequency fi for block b
    m0 = np.trapz(E,freq) #Spectral moment
    H_m0 = 4*np.sqrt(m0/(9.81*1025)) #Course approximation significant wave height [m]
    Tp = 5*np.sqrt(H_m0) #Peak period of spectrum [s]
    #http://www.coastalwiki.org/wiki/Statistical_description_of_wave_parameters
    Hrms = np.sqrt(m0*8/(9.81*1025)) #Root mean square wave height [m]
    H_s = 1.42*Hrms #Significant wave height if Reynolds distribution [m]
    av_eta = np.mean(np.abs(eta)) #Average wave elevation [m]
    # E = np.mean(E,axis=1)/d_f
    Eta = np.sqrt((A**2 + B**2))*2
    Eta = np.sort(Eta)
    H_13 = np.mean(Eta[len(Eta)*2//3:]*2)
    #Confindence interval
    #MORE HERE
    if visual == 1:
        plt.figure()
        plt.plot(freq,E,'.')
        plt.ylabel('Energy density [m^2/Hz]')
        plt.xlabel('Frequency [Hz]')
        plt.xlim(0,10)
        plt.legend(['E'],loc='upper right')

    return  Tp, H_m0, Hrms, H_s, H_13, av_eta

import numpy as np
filepath = '/home/anna/Documents/1Work_in_progress/WaveFilesIrregularFarkas/02_jonswap_tpk1.15_hs0.04.txt'
f = open(filepath,"r") #create csv file
amplitude = f.read() #amplitude data
ampl = amplitude.split()
ampl = np.array(ampl,dtype=float) #convert to list of floats
f.close() #close the file
ratio_a_V = 0.0442 #Ratio of wavemaker amplitude to volts
Tp = SpectrumData(ampl,0)
w = 2*np.pi/Tp[0] #Peak wave frequency [rad/s]
Uc = 0 #Current velocity
if Uc == 0:
    ratio_a_s = 1.36E-04*w**3 - 9.77E-03*w**2 + 2.15E-01*w - 5.07E-01
if Uc == 0.3:
    ratio_a_s = 6.69E-05*w**3 - 5.67E-03*w**2 + 1.53E-01*w - 3.72E-01
if Uc == 0.5:
    ratio_a_s =  4.64E-05*w**3 - 4.38E-03*w**2 + 1.32E-01*w - 3.27E-01
amplitude = ampl*ratio_a_V*1000*ratio_a_s #wave amplitude [m]
Tp,H_m0, Hrms, H_s, H_13, av_eta = SpectrumData(amplitude,1)

# %%
