#%%
import module_CheckWavefile
from imp import reload
reload(module_CheckWavefile)
from module_CheckWavefile import FindMaxValues

import glob
files = glob.glob("/home/anna/Documents/1Work_in_progress/WaveFilesIrregularFarkas/*.txt") #find all tdms files in a certain folder
# files = glob.glob("/home/anna/Documents/1Work_in_progress/Programming/WaveFiles/*.txt") #find all tdms files in a certain folder
files.sort()

Tp = 1.4 #Peak wave period [s] (needed for the transfer function)
ratio_s_V = 0.0422 #4.22 mm/volt (should check with Farkas) Sleeptank value
# ratio_s_V  = 0.0125#DUMMY VALUE 0.125 #0.125 m/volt 10V max = 125 mm max Flumetank value
Uc = 0.5 #Current velocity [m/s]
maxS,maxV,maxA,maxEta = FindMaxValues(files,Tp,Uc,ratio_s_V,1)

# %%
