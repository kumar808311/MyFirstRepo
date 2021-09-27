# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 17:09:06 2020

@author: H177625
"""



import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

MemoryBlockAllocationTime = np.genfromtxt('C:\LogFile\ODASSEA3\PT1\Managed Memory Block Allocation Time.txt', delimiter=',')
MemoryBlockCopyingTime = np.genfromtxt('C:\LogFile\ODASSEA3\PT1\Managed Memory Block CopyingTime.txt', delimiter=',')
WaitReleaseDigiData = np.genfromtxt('C:\LogFile\ODASSEA3\PT1\WaitTimeReleaseDigiData.txt', delimiter=',')
WaitGetDigiData = np.genfromtxt('C:\LogFile\ODASSEA3\PT1\WaitTimeGetDigiData.txt', delimiter=',')

a,b,c,d=[],[],[],[]
BlockAllocation, BlockCopying, ReleaseDigiTime, GetDigiData =[], [], [], [] 

a = MemoryBlockAllocationTime[:,0]
b =MemoryBlockCopyingTime[:,0]
c= WaitReleaseDigiData[:,0]
d= WaitGetDigiData[:,0]

BlockAllocation = MemoryBlockAllocationTime[:,1]
BlockCopying = MemoryBlockCopyingTime[:,1]
ReleaseDigiTime = WaitReleaseDigiData[:,1]
GetDigiDataTime = WaitGetDigiData[:,1]


fig=plt.figure()
fig.subplots_adjust(hspace=0.5)  # Add Spacing between SubPlots for X axis label. 


plt.subplot(411)

plt.plot(a, BlockAllocation, 'o', markersize=np.sqrt(5.), color='black');
plt.grid(b=True, which='major', color='k', linestyle='-',alpha=0.1)
plt.grid(b=True, which='minor', color='r', linestyle='-', alpha=0.1)
plt.minorticks_on()   
plt.title('  Managed Memory Block Allocation Time (ms) ', fontsize =12, color='blue' )
#plt.xlabel( 'Sweeps #', fontsize = 12, color='black')
plt.ylabel(' Tiime  (ms)', fontsize = 12,color='black')


figure=plt.gcf()
figure.set_size_inches(10,10)
#plt.savefig('C:\LogFile\Managed Memory Block Allocation Time ',dpi=125)


plt.subplot(412)

plt.plot(b, BlockCopying, 'o',  markersize=np.sqrt(5.), color='magenta');
plt.grid(b=True, which='major', color='k', linestyle='-',alpha=0.1)
plt.grid(b=True, which='minor', color='r', linestyle='-', alpha=0.1)
plt.minorticks_on()   
plt.title(' Managed Memory Block Copying Time (ms) ', fontsize =12, color='blue' )
#plt.xlabel( 'Sweeps #', fontsize = 12, color='black')
plt.ylabel(' Tiime  (ms)', fontsize = 12,color='black')
#plt.savefig('C:\LogFile\Managed Memory Block Copying Time ',dpi=125)      


plt.subplot(413)

plt.plot(c, ReleaseDigiTime, 'o',  markersize=np.sqrt(5.), color='blue');
plt.grid(b=True, which='major', color='k', linestyle='-',alpha=0.1)
plt.grid(b=True, which='minor', color='r', linestyle='-', alpha=0.1)
plt.minorticks_on()   
plt.title('  Waiting time to release Digitizer data (ms) ', fontsize =12, color='blue' )
#plt.xlabel( 'Sweeps #', fontsize = 12, color='black')
plt.ylabel('Time (ms)', fontsize = 12,color='black')
#plt.savefig('C:\LogFile\Waiting time to releaae Digitizer data ',dpi=125)      
     


plt.subplot(414)

plt.plot(d, GetDigiDataTime, 'o', markersize=np.sqrt(5.), color='blue');
plt.grid(b=True, which='major', color='k', linestyle='-',alpha=0.1)
plt.grid(b=True, which='minor', color='r', linestyle='-', alpha=0.1)
plt.minorticks_on()   
plt.title('  Waiting time to get data from Digitizer (ms) ', fontsize =12, color='blue' )
#plt.xlabel( 'Sweeps #', fontsize = 12, color='black')
plt.ylabel('Time (ms)', fontsize = 12,color='black')


figure=plt.gcf()
figure.set_size_inches(10,10)
plt.savefig('C:\LogFile\ODASSEA3\PT1\PLOT2 ',dpi=125)

plt.show ()

 ## Log Metrics { Minimum, Maximum, and Average No# } 

MinBAL=min(BlockAllocation [1:])
MaxBAL= max(BlockAllocation [1:])
AvgBAL = sum(BlockAllocation[1:])/len(BlockAllocation[1:])

# print(MinBAL)
# print(MaxBAL)
# print(AvgBAL)

MinBCopy = min(BlockCopying[1:])
MaxBCopy= max(BlockCopying[1:])
AvgBCopy = sum(BlockCopying[1:])/len(BlockCopying[1:])

# print(MinBCopy)
# print(MaxBCopy)
# print(AvgBCopy)


MinRDigiTime = min(ReleaseDigiTime[1:])
MaxRDigiTime= max(ReleaseDigiTime[1:])
AvgRDigiTime= sum(ReleaseDigiTime[1:])/len(ReleaseDigiTime[1:])

# print(MinBCopy)
# print(MaxBCopy)
# print(AvgBCopy)


MinGetDTime = min(GetDigiDataTime[1:])
MaxGetDTime= max(GetDigiDataTime[1:])
AvgGetDTime= sum(GetDigiDataTime[1:])/len(GetDigiDataTime[1:])

print( "       "        " Memory Block Allocation time  (ms)"   "    "        "Memory Block Copying time (ms)" "  "  " Release Digitizer Data Time  (ms)"  "  "      " Get Digitizer Data (ms)", '\n'
      "Minimum =",           MinBAL, "                              ",  MinBCopy,"                              ", MinRDigiTime,"                                 ",  MinGetDTime, '\n'
      "Maximum =",           MaxBAL, "                           ",  MaxBCopy,"                            ",   MaxRDigiTime , ",                                ", MaxGetDTime, '\n'
      "Average =",           round(AvgBAL,3), "                            ", round(AvgBCopy,3),  "                           ",  round(AvgRDigiTime,3),  ",                                ", round(AvgGetDTime,3))


