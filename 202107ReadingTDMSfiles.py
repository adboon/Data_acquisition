# Reading in TDMS files in Python
# PhD project Anna Boon
# 2021 07 19

#%%
# from https://pypi.org/project/npTDMS/
# Obtaining the data from TDMS files
from nptdms import TdmsFile

D_temp = list()
# filepath = "LabVIEW\DataTest\_WPB_2021_07_19_11_36_55.tdms"
filepath = "U:\staff-umbrella\WPB Data\TestLabVIEW\_NAME_2021_07_19_16_58_28.tdms"
tdms_file = TdmsFile.read(filepath)
metadata = TdmsFile.read_metadata(filepath)
for group in tdms_file.groups():
    group_name = group.name
    for channel in group.channels():
        channel_name = channel.name
        # Access dictionary of properties:
        properties = channel.properties
        # Access numpy array of data for channel:
        data = channel[:]
        D_temp.append(data[:])


time = channel.time_track()

import matplotlib.pyplot as plt

plt.figure()
plt.plot(time[1:1000],D_temp[0][1:1000])#,data[0:10000])





    
  #  group = tdms_file['group name']
# %%

# Allows you to see all the groups and channels in a file 
with TdmsFile.open(filepath) as tdms_file:
    all_groups = tdms_file.groups() #Allows you to see all the groups in the file
    group = tdms_file["Untitled"]
    all_channels = group.channels() #Allows you to see all channels in a group
# %%
