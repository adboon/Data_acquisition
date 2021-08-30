#%%
import module_CheckWavefile
from imp import reload
reload(module_CheckWavefile)
from module_CheckWavefile import FindMaxValues

import glob
files = glob.glob("/home/anna/Documents/1Work_in_progress/WaveFilesIrregularFarkas/*.txt") #find all tdms files in a certain folder
files.sort()

ratio_a_V = 0.0422 #4.22 mm/volt (should check with Farkas)


maxS,maxV,maxA,masEta = FindMaxValues(files[0:4],ratio_a_V,1)

# %%
