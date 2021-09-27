# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 17:09:06 2020

@author: H177625
"""
import numpy as np 
import matplotlib.pyplot as plt

#WrittenDiskData = np.genfromtxt('C:\LogFile\ODASSEA3\PT1\WrittenDiskTime.txt', delimiter=',');
#GPUPhaseComputation = np.genfromtxt('C:\LogFile\ODASSEA3\PT1\GPU Phase Computation Time.txt', delimiter=',');
#PhaseComputationTimeForChunk = np.genfromtxt('C:\LogFile\ODASSEA3\PT1\Phase Calculate Time For Chunk.txt', delimiter=',');

WrittenDiskData = np.genfromtxt('C:\LogFile\ODASSEA3\Sep23\WrittenDiskTime.txt', delimiter=',');
GPUPhaseComputation = np.genfromtxt('C:\LogFile\ODASSEA3\Sep23\GPU Phase Computation Time.txt', delimiter=',');
PhaseComputationTimeForChunk = np.genfromtxt('C:\LogFile\ODASSEA3\Sep23\Phase Calculate Time For Chunk.txt', delimiter=',');


x=[]
y=[]
z=[]

DiskTime, GPUPhase, PhaseComChunk =[], [], [] 
DiskTimeFor1sDataBlock=[]
PhaseCompFor1sDataBlock=[]

x = WrittenDiskData[:,0]
y = GPUPhaseComputation[:,0]
z = PhaseComputationTimeForChunk[:,0]


DiskTime = WrittenDiskData[:,1]



GPUPhase = GPUPhaseComputation[:,1]
PhaseComChunk = PhaseComputationTimeForChunk[:,1]

GPUPhaseFor1sDataBlock=[]

# Performance numbers scale to 1s of data block

# Calculation for Scaling facotr ( 3.72)
# File Size Calculation =  FramesPerBuffer * Total no# of channels * Data Type ( For Short -2 and float=4) 
####  For Example  Optical Pulse Rate=10 kHz, Start Channel =1 and End Channel=9728, FramePerBuffer=2688
# File Size =  2688 * 9728 * 2 = 52,297,728 Bytes 
#  Recording time in each file =  FramePerBuffer /  Optical Pulse Frequency 
####  Recording time in each file=  2688 / 10,000 = 0.2688s 
#  Scaling factor  calculation for 1s of data block :- ( 1/ Recording time in each file )
###  Scaling Factor = 1/ 0.2688 = 3.72 


##  For  8kHz Start Channel=1 and End Channel=12032 FramePerBuffere is 2176
# Scaling factor is  3.67 for GPU Phase and PhaseComChunk

## 10 kHz with 9728 Channels, it is 3.72 

GPUPhaseFor1sDataBlock=3.72*GPUPhase
PhaseCompFor1sDataBlock=3.72*PhaseComChunk
DiskTimeFor1sDataBlock= 1.24*DiskTime

#GPUPhaseFor1sDataBlock=2.69*GPUPhase
#PhaseCompFor1sDataBlock=2.69*PhaseComChunk
#DiskTimeFor1sDataBlock= 0.90* DiskTime



ProcessingDataStorage=[]
ProcessingDataStorage = np.maximum(PhaseCompFor1sDataBlock, DiskTimeFor1sDataBlock)


## PLOT Data Processing and Data Storage 


fig=plt.figure()
fig.subplots_adjust(hspace=0.5)  # Add Spacing between SubPlots for X axis label. 
fig.set_size_inches(17.0, 14.0)


plt.subplot(211)
plt.rc('xtick',labelsize=15)
plt.rc('ytick',labelsize=15)

plt.plot(x, ProcessingDataStorage, 'o', markersize=np.sqrt(20), color='blue');
plt.grid(b=True, which='major', color='k', linestyle='-',alpha=0.1)
plt.grid(b=True, which='minor', color='r', linestyle='-', alpha=0.1)
plt.minorticks_on()   
plt.title('  Data Processing & Disk Storage ', fontsize =20, fontweight='bold', color='Black', y=1.05 )
plt.xlabel( ' Data Acquisition Time ', fontsize = 20, fontweight='bold', color='black')
plt.ylabel('Time (ms)', fontsize = 20, fontweight='bold', color='black')
plt.ylim((100,4500))

#GPU Phase Computational Time (ms)

plt.subplot(212)
plt.subplots_adjust(top=0.7) 
plt.rc('xtick',labelsize=15)
plt.rc('ytick',labelsize=15)
plt.ylim((10,250))

#plt.plot(x, GPUPhaseFor1sDataBlock, 'o',  color='blue');

plt.plot(x, GPUPhaseFor1sDataBlock, 'o', markersize=np.sqrt(20.), color='blue');
plt.grid(b=True, which='major', color='k', linestyle='-',alpha=0.1)
plt.grid(b=True, which='minor', color='r', linestyle='-', alpha=0.1)
plt.minorticks_on()  
plt.title('  GPU Phase Computational Time (ms) ', fontsize =20, fontweight='bold', color='black', y=1.05 )
plt.xlabel( ' Data Acquisition Time ', fontsize = 20, fontweight='bold', color='black')
plt.ylabel(' Tiime  (ms)', fontsize = 20, fontweight='bold', color='black')
   
plt.savefig('C:\LogFile\ODASSEA3\Sep23/Data Processing & Data Storage_Limit ',dpi=125)  

 # Log Metrics { Minimum, Maximum, and Average No# } 

MinGPUTime =min(GPUPhaseFor1sDataBlock [1:])
MaxGPUTime = max(GPUPhaseFor1sDataBlock [1:])
AvgGPUTime = sum(GPUPhaseFor1sDataBlock [1:])/len(GPUPhaseFor1sDataBlock [1:])

 
MinDiskTime = min(ProcessingDataStorage[1:])
MaxDiskTime= max(ProcessingDataStorage[1:])
AvgDiskTime= sum(ProcessingDataStorage[1:])/len(ProcessingDataStorage[1:])


print('\n', "Performance Report [ Pulse Rate:- 10 kHz, Start Channel =1, End Channel =9728, File Format :- BIN, Data Format :- Delta Phase,  Weight Scheme = IQ Radius ] :- ")

print( "       "                  " GPU Phase Computation Time (ms)"   "                           "                                             " Data Processing & Disk Storage (ms)", '\n'
      "Minimum =",                       round(MinGPUTime,3),"                                                       ",        round(MinDiskTime,3), '\n'
      "Maximum =",                        round(MaxGPUTime,3), "                                                       ",          round (MaxDiskTime,3), '\n'
      "Average =",                       round(AvgGPUTime,3), "                                                         ",  round(AvgDiskTime,3))



