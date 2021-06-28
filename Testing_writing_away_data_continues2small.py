# Testing opening a file which is open somewhere else, taking the data and saving it in separate timestamped files
# Anna Boon PhD research
# 25-06-2021
#%%
# Saving part of original file away
# Parts of code from https://stackoverflow.com/questions/2274503/reading-binary-file-in-python

import datetime as dt
import struct
import os

# Parameters and initializing
dt = dt.datetime.now() #Register current time
timestamp = dt.strftime("%Y%m%d-%H_%M_%S") #Timestamp for file and filename
Data = [] #Create empty file to store data
bin_size = 8 #Size of the binary numbers

# Files and filenames
fname = ('TestData/Testfile_continues_data.bin') #Name of the file that will be opened
f = open(fname,"rb") #Open file with allll the data
fsave = ('TestData/Testfile_part_data',timestamp,'.csv') #Name of the file that will be opened
fsave = ''.join(fsave) #Converting the name of the file from a tuple to a string
filesave = open(fsave,"w+") #Open file where part of data is going to be saved
fnext = open('TestData/Next_round_start.txt',"r") #Open file where the starting point for next round is saved

# Here last_written from last time is imported
last_written = fnext.read() #Number from a file to keep track what is already written away and what not
fnext.close()
if os.stat('TestData/Next_round_start.txt').st_size == 0:
    last_written = 0
start_bin = int(last_written)*bin_size #Convert it to the bin location
size_file = os.path.getsize(fname) #Find out size of file so only necessary part is opened
# Read data from the large, active file
with f as inh:
    inh.seek(start_bin) #Find the start of the new data
    data = inh.read(size_file - start_bin) #Open the new part of the data
for i in range(0, len(data), bin_size): #Convert that part of the data to int
    pos = struct.unpack('<q', data[i:i+bin_size]) #q = 8bin, < = 'little', with a buffer, only unpacks the part of the data in which I am intrested this go around      
    Data.append(pos[0]) #Save the converted data to Data

with open(fsave,'w') as f: #Open the new file
    f.write(timestamp) #Stamp the time
    for item in Data: #For every line of the data
        f.write("%s\n" % item) #ADDAPT Write it in the file (change the writing format depending on the data)
filesave.close() #Close the file

# Write away the value of last_written to a file where it can be picked up again for the next go around
fnext = open('TestData/Next_round_start.txt',"w") #Open file where the starting point for next round is saved
last_written = Data[-1]
fnext.write(str(last_written))
fnext.close()
# %%


