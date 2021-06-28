# Data acquisition testing
# Anna Boon thesis
# 25-06-2021

#%%
import matplotlib.pyplot as plt

Runs = [592, 593]
run_nr = Runs[1]

#FROM HERE ON POSSIBLY MAKE IT A FUNCTION WITH RUN AS INPUT
import numpy as np
from collections import defaultdict
import pandas as pd

D = data = defaultdict(list) #Make a dictionary out of D to save the various Src file data within
nchan = [9, 3] #number of channels in Src[i] type file (amount of values should be equal to amount of types of files)
#Loading in logboek data
Logboek = pd.read_excel(r'TestData/TestLogboek.xlsx') #Read in as a DataFrame with pandas
Logboek = Logboek.values.tolist() #Convert from a DataFrame to a list
for i in range(1,len(Logboek)): #Search within the rows of excel to the run
    if Logboek[i][0] == run_nr: #When run is found
        Offset = [Logboek[i-1][1:9], Logboek[i-1][9:11]] #Use the previous zero run as offset in further calculations (devision made based on channels and distribution of those over Src files)

for i in range(0,len(nchan)): #For each number of Src file
    fname = ('TestData/202010-Run',str(run_nr),'_Src',str(i+1),'.bin') #Name of the file that will be opened
    fname = ''.join(fname) #Converting the name of the file from a tuple to a string
    D_temp = np.fromfile(fname, dtype='float32') #Loading in data, dtype = 32 for towing tank, 64 for ComFLOW
    D[i] = D_temp.reshape(-1,nchan[i]) #Reshape depending on the amount of channels (=nchan), saving in the dictionary D
    D[i][:,1:nchan[i]] = D[i][:,1:nchan[i]] - Offset[i] #Substract the offset measured during zero run from the measurements
        
time1 = D[0][:,0]
time2 = D[1][:,0]
velocity = D[1][:,2]
force = D[0][:,6] + D[0][:,7] - D[0][:,8]
position = D[1][:,1]

# #%%
    #Plotting results
    #Src1: channels: 0)Time 1)Velocity (wheel) 2)Wave maker 3)Wave probe 4)Wave probe 5)Reference 6)Force 7)Force 8)Force  
    #Src2: channels: 0)Time 1)Position cart 2)Velocity (laser) 

plt.figure(1)
plt.plot(time2,-position)
plt.figure(2)
plt.plot(time1,force)













# %%
