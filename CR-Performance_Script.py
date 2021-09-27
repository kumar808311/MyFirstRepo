import os 
import pandas as pd
import re
import glob 
#import csv


## The following Performance Parameter can be extracted from FiberVSP log

# GPU Phases computation time
# Managed memory block allocation time
# Phases calculated for chunk
# Managed memory block copying time
# Waiting time to release Digitizer data
# Waiting time for get data from digitizer in
# Written on disc in
# GPU Memory copy in time

# Processing Multiple Files and Writing Files.

# Set the folder path where all ODASSEA logs files are available.  
# In order to get all of the files which match a specific pattern, we will use the wildcard character *.

file_location = os.path.join('C:\LogFile\ODASSEA3', 'Sep23','*.log.*')
print('\n', "Directory Path")
print(file_location)      
   

filenames = glob.glob(file_location)
filenames.sort(key=lambda f: int(re.sub('\D', '', f)))  
file_count=len(filenames)
#filenames = glob.glob(file_location)
print('\n', "Printing All files in the directory")
print('\n', filenames)


print(" Total file in the directory :- ", file_count)

Out_file1_location="C:\LogFile\ODASSEA3\Sep23/Phase Calculate Time For Chunk.txt"
Out_file2_location="C:\LogFile\ODASSEA3\Sep23/GPU Phase Computation Time.txt"
Out_file3_location="C:\LogFile\ODASSEA3\Sep23/WrittenDiskTime.txt"



#Out_file1_location="C:\LogFile\PerformanceTest/ServerLog/Phase Calculate Time For Chunk.txt"
#Out_file2_location="C:\LogFile\PerformanceTest/ServerLog/GPU Phase Computation Time.txt"
#Out_file3_location="C:\LogFile\PerformanceTest/ServerLog/WrittenDiskTime.txt"



PhaseTime =[]
GPU=[]
GPU_Out=[]
MMBAT=[]
PhaseForChunk=[]
BlockCopyingTime=[]
WaitTimeToReleaseDigitizerData=[]
WaitTimeToGetDigitizerData=[]
WrittenDiskTime=[]

linenum = 0
substr_PhaseTime = "GPU Phases computation time"
substr_PhaseForChunk="Phases calculated for chunk"
substr_WrittenDiskTime="written on disc in"

# GPU Phases Computation time

for f in filenames:                    #
    outfile=open(f,'rt')
    myfile=outfile.readlines()
   # outfile.close()
    
## Parsing forr PhasesCompTimeForChunk, Phase Comp Time, and WrittenDiskTime
    for line in myfile: 
        index = line.find(substr_PhaseForChunk)
        index02 = line.find(substr_PhaseTime)
        index03 = line.find(substr_WrittenDiskTime)
        
        if (index != -1):
            index2 = line.find("in", index + len(substr_PhaseForChunk))
            time = re.search(r'\d+', line[index2:]).group()
            PhaseForChunk.append(time)
            
        if (index02 != -1):
            time = re.search(r'\d+', line[index02:]).group()
            PhaseTime.append(time)
          
        
            
        if (index03 != -1):
            time = re.search(r'\d+', line[index03:]).group()
            WrittenDiskTime.append(time)

df_PhaseForChunk=pd.DataFrame(PhaseForChunk,columns=['PhasesCompTimeforchunk'])
df_merge1 = pd.concat([df_PhaseForChunk], axis=1, sort=False)
df_merge1.to_csv(Out_file1_location)

    
df_phase=pd.DataFrame(PhaseTime,columns=['PhaseCompTime'])
df_merge2 = pd.concat([ df_phase], axis=1, sort=False)
df_merge2.to_csv(Out_file2_location)


df_WrittenDiskTime=pd.DataFrame(WrittenDiskTime,columns=['WrittenDiskTime'])
df_merge3 = pd.concat([ df_WrittenDiskTime], axis=1, sort=False)
df_merge3.to_csv(Out_file3_location)

outfile.close()