# Working with data template
# PhD research Anna Boon
# 28-07-2021


#%%
## Create file to save the identified events to
import csv
file_events = "IdentifiedEvents.csv" #name of file
f = open(file_events,"w+") #create csv file
f.write(str()) #empty the data in the file
f.close() #close the file


##%%
## Files that should be opened
import glob
files = glob.glob("/home/anna/Documents/1Work_in_progress/DataTest/*.tdms") #find all tdms files in a certain folder
files.sort()

##%%
## Obtaining the data from TDMS files
# from https://pypi.org/project/npTDMS/
from nptdms import TdmsFile
import numpy as np

D_temp = list() #Make empty list for data to append to
Name = list() #Make empty list to append channel names to

for filepath in files:

    D_temp = list() #Make empty list for data to append to
    Name = list() #Make empty list to append channel names to

    tdms_file = TdmsFile.read(filepath) #Open the TDMS file
    metadata = TdmsFile.read_metadata(filepath) #Get metadata (dont understand this)
    for group in tdms_file.groups(): #Do for all groups in a file
        group_name = group.name #Find each group within a file
        for channel in group.channels(): #Do for all channels in a group
            channel_name = channel.name #Find each channel name 
            Name.append(channel_name) #Make list of all channel names
            # Access dictionary of properties:
            properties = channel.properties #Gives you information about the file (also units)
            # Access numpy array of data for channel:
            data = channel[:] #rename it to data
            D_temp.append(data[:]) #append to other data (will become long 1D array)
        
    time = channel.time_track() #saved separatly the relative time [s]

    # HERE YOU CAN ADD CODE TO FIND CERTAIN DATA FROM THE FILE YOU OPENED. 
    # EXAMPLE: FIND THE TIMESTAMP AND ALL DATA VALUES WHEN THE DATA IN THE FIRST COLUMN IS ABOVE 4.5
    # ALSO, SAVE THE DATA THAT FULFILLS THE SELECTED CRITERIA TO A SEPARATE FILE
    column_interest = D_temp[0] #Column in which certain data should be identified
    cutoff_value = 9.9 #Value above which data should be saved
    indexes = [i for i,x in enumerate(column_interest) if x > cutoff_value] #Find the index of all values larger than 4.5
    f = open(file_events, "a") #Identifier to append data to file
    writer = csv.writer(f)
    for index in indexes: #For each index
        f.write('{:.3e}'.format(time[index])) #time written in first column
        f.write(',') #tab
        row = [] #make sure row that is generated to be written is empty
        for ii in range(0,len(D_temp)): #For each column with data
            row.append(D_temp[ii][index]) #fill row to be written
        writer.writerow(row) #write the data in scientific format with 5 digits
        # f.write('\n') #newline after writing everything from a certain index TWO DIFFERENT TYPE OF SEPERATORS DOESN'T WORK FOR CSV READING
    f.close()


print('Done')




# %%
#Test is if data is written away as I want
import pandas as pd

events = pd.read_csv(file_events).to_numpy() #read in data from file
print('file read')
# events = np.reshape(events,(4,-1)) #reshape


import matplotlib.pyplot as plt

plt.figure()
plt.plot(events[:,0],events[:,1],'.')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# %%
