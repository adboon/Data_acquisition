

def readingTDMSfile(filepath):
  # from https://pypi.org/project/npTDMS/
  # Obtaining the data from TDMS files
  from nptdms import TdmsFile

  Data = list() #Make empty list for data to append to
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
          Data.append(data[:]) #append to other data (will become long 1D array)


  time = channel.time_track() #saved separatly the relative time [s]
  return group_name, properties, Name, Data, time
# #%%

def plottingTDMSfile(filepath,resolution):
    from nptdms import TdmsFile

    Data = list() #Make empty list for data to append to
    Name = list() #Make empty list to append channel names to
    tdms_file = TdmsFile.read(filepath) #Open the TDMS file
    for group in tdms_file.groups(): #Do for all groups in a file
      group_name = group.name #Find each group within a file
      for channel in group.channels(): #Do for all channels in a group
          channel_name = channel.name #Find each channel name 
          Name.append(channel_name) #Make list of all channel names
          # Access dictionary of properties:
          properties = channel.properties #Gives you information about the file (also units)
          # Access numpy array of data for channel:
          data = channel[:] #rename it to data
          Data.append(data[:]) #append to other data (will become long 1D array)
    time = channel.time_track() #saved separatly the relative time [s]

#Plotting the results
    import matplotlib.pyplot as plt 

#Parameters to fill in
    t_start = 0 #start element of time that is plotted [#]
    t_end = len(time) #last element of time that is plotted [#]
    t_int = int(resolution) #interval of plotted points [#]
    points = range(t_start,t_end,t_int) #what will be plotted
#Making figure
    plt.figure()
    plt.title(group_name)
    for i in range(0,len(Name)):
      plt.plot(time[points],Data[i][points])
      plt.xlabel('Time [s]')
      plt.ylabel('Amplitude')   
      plt.legend(Name, loc='upper left')
      




    
#   #  group = tdms_file['group name']
# # %%

# # Allows you to see all the groups and channels in a file 
# with TdmsFile.open(filepath) as tdms_file:
#     all_groups = tdms_file.groups() #Allows you to see all the groups in the file
#     group = tdms_file["Untitled"]
#     all_channels = group.channels() #Allows you to see all channels in a group
# # %%

