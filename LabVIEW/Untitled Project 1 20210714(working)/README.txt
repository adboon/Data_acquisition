# FLUME TANK DATA ACQUISITION SYSTEM AND WAVE MAKER CONTROL SYSTEM
# by ANNA BOON for PHD RESEARCH on 14-07-2021

The flume tank has existed for quite some time now, but resently, for the PhD research, a wavemaker was added. 
Because of the type of research that is planned on (long running experiments), a stable data acquisition system is also needed.
At the flume tank there is a computer with OS Windows and a internet connection, a NI DAQ 6009, and a compactRIO. 
With this system the wavemaker can be controlled and data acquired.


1) Activate in Task Scheduler the system that will write away files to an offsite location <<<<<<<<ADD PROGRAMME NAME HERE, OR EVEN EXACT SCRIPT THAT SHOULD BE COPIED>>>>>>>>>>>>>>>>
2) In case you want to make waves, create a file with voltages between -10&+10V (min and max position = 12 cm underwater - 1 cm underwater)
    The data should be 100 Hz in text file with after every voltage a new line (<VOLTAGE>\n)
3) Start the programme <<<<<<<<<<<<<<<ADD NAME OF FLUME TANK PROGRAMME>>>>>>>>>>>>>>>>>>>

NOTE: The offsite path in this programme should lead to a local folder. The path of where to get the files in the programme of step 1 should be changed to the path of this folder.			
