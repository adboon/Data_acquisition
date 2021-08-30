# Reading in TDMS files in Python
# PhD project Anna Boon
# 2021 07 19

#%%
from FunctionTDMSfile import *
filepath = "/home/anna/Documents/1Work_in_progress/Programming/_NAME_2021_07_19_16_59_12.tdms"
# filepath = "davs://adbo@nextcloud.dragundo.net/remote.php/webdav/Documents/PhD/3Programming/LabVIEW/DataTest/_NAME_2021_07_19_16_59_12.tdms" #Path to file and filename

group_name, properties, Name, Data, time = readingTDMSfile(filepath)


plottingTDMSfile(filepath,1050) #filepath, resolution (steps that are plotted (1 = every step, 100 = every 100 steps))






# %%
