# Reading the testing files in .bin format
# PhD Anna Boon
# 28-06-2021

#%%
import numpy as np
import struct

nchan = 1
Data = []
fname = ('Testfile_continues_data.bin') #Name of the file that will be opened
file = open(fname,"rb")
with file as f:
    while (byte := f.read(8)):
        Data.append(int.from_bytes(byte,byteorder='little'))



# %%