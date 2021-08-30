# Read binary LabVIEW files
# PhD thesis Anna Boon
# 20210719

#%%
# parts from https://shocksolution.com/2008/06/25/reading-labview-binary-files-with-python/
# Parts of code from https://stackoverflow.com/questions/2274503/reading-binary-file-in-python
# DIT WERKT NOG HELEMAAL NIET, KRIJG IETS MAAR NIET WAT HET ZOU MOETEN ZIJN
import numpy as np
import matplotlib.pyplot as plt
import struct
# Parameters and initializing

# Files and filenames
# path to labview file /home/anna/natinst/LabVIEW Data/Testing_project/Testing_project_continues_data.lvproj
fname = ("TestLabVIEW\WPB_2021_07_19_12_07_25.bin") #Name of the file that will be opened
f = open(fname,mode="rb") #Open file with all the data
data1 = struct.unpack('>d', f.read(8))
Data2 = np.fromfile(fname, dtype='int8')
data2 = Data2.reshape(-1,4)
plt.figure()
plt.plot(data1)
plt.figure()
plt.plot(data2)

# %%
