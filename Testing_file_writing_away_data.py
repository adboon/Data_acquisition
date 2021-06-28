# Attempting to generate a test file with continues data comming in so I can try and see if I can safe that data to separate files, with time stamps etc.
# Anna Boon PhD research
# 25-06-2021

#%%
a = 1
import datetime as dt

# Opening the file in which data is continuesly written
file = open("TestData/Testfile_continues_data.bin","wb")

# Save the current time to a variable ('t')
t = dt.datetime.now()
n = 1
while a == 1:
    delta = dt.datetime.now()-t
    if delta.seconds >= 3:
        file.write(n.to_bytes(2,'big'))
        n =+ 1
        print('done')
        # Update 't' variable to new time
        t = dt.datetime.now()
 


# %%

