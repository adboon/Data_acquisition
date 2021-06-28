# Attempting to generate a test file with continues data comming in so I can try and see if I can safe that data to separate files, with time stamps etc.
# Anna Boon PhD research
# 25-06-2021

#%%

import datetime as dt

# Opening the file in which data is continuesly written
file = open("TestData/Testfile_continues_data.bin","wb")
# Save the current time to a variable ('t')
t = dt.datetime.now()
n = 0
while True:
    delta = dt.datetime.now()-t
    if delta.seconds >= 1:
        bytes = n.to_bytes(8, 'little')
        file.write(bytes)
        file.flush()
        n = n + 1
        t = dt.datetime.now()
        if n >= 1000:
            file.close
            print('done')
            break

    

# %%

