# Run this before the start of the experiment
# It will set everything back to what it should be
# Anna Boon PhD research
# 28-06-2021

#%%
# ADD HERE ALSO SOME THINGS TO MAKE SURE NOTHING GETS OVERWRITTEN OF DESTROYED

# Reset the last_written back to 0
fnext = open('TestData/Next_round_start.txt',"w") #Open file where the starting point for next round is saved
fnext.write(str(0))
fnext.close()



# %%
