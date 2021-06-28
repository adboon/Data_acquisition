# Testing opening a file which is open somewhere else, taking the data and saving it in separate timestamped files
# Anna Boon PhD research
# 25-06-2021


# Wat er nog gebeuren is dat het eerst nog moet werken (write functie werkt nog niet)
# Belangrijk ook: op dit moment wordt alles  wat er uberhaupt in de grote file wordt weggeschreven nog eens dubbel weggeschreven maar dit moet aangepast worden zodat alleen de nieuwe data in de nieuwe file wordt weggeschreven

#%%
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import pandas as pd
import datetime as dt

fname = ('TestData/Testfile_continues_data.bin') #Name of the file that will be opened

t = dt.datetime.now()
while True:
    delta = dt.datetime.now()-t
    if delta.seconds >= 10:
        filename = ('TestData/Test_data_noncontinues',str(dt.datetime.now()),'.csv')
        filename = ''.join(filename)
        file = open(filename,"w+")
        Data = np.fromfile(fname, dtype='float32') #Loading in data, dtype = 32 for towing tank, 64 for ComFLOW
        file.write([dt.datetime.now(),Data])
        file.close()
        # Update 't' variable to new time
        t = dt.datetime.now()







#%%
# displaying the contents
print("\nBefore flush():\n", fileContent)
# clearing the input buffer
fileObject.flush()
# reading the contents after flush()
# reads nothing as the internal buffer is cleared
fileContent = fileObject.read()
  
# displaying the contents
print("\nAfter flush():\n", fileContent)
  
# closing the file
fileObject.close()