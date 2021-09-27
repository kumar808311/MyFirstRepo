# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 17:09:06 2020

@author: H177625
"""



import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

WrittenDiskData = np.genfromtxt('C:\LogFile\ODASSEA3\Sep23\WrittenDiskTime.txt', delimiter=',');
GPUPhaseComputation = np.genfromtxt('C:\LogFile\ODASSEA3\Sep23\GPU Phase Computation Time.txt', delimiter=',');
PhaseComputationTimeForChunk = np.genfromtxt('C:\LogFile\ODASSEA3\Sep23\Phase Calculate Time For Chunk.txt', delimiter=',');


x=[]
y=[]
z=[]

DiskTime, GPUPhase, PhaseComChunk =[], [], [] 


x = WrittenDiskData[:,0]
y = GPUPhaseComputation[:,0]
z = PhaseComputationTimeForChunk[:,0]



DiskTime = WrittenDiskData[:,1]
GPUPhase = GPUPhaseComputation[:,1]
PhaseComChunk = PhaseComputationTimeForChunk[:,1]
 

fig=plt.figure()
fig.subplots_adjust(hspace=0.5)  # Add Spacing between SubPlots for X axis label. 
fig.set_size_inches(20.0, 20.0)

## GPU Phase Computational Time (ms)

plt.subplot(311)
plt.plot(x, GPUPhase, 'o',  markersize=np.sqrt(5.), color='black');
plt.grid(b=True, which='major', color='k', linestyle='-',alpha=0.1)
plt.grid(b=True, which='minor', color='r', linestyle='-', alpha=0.1)
plt.minorticks_on()   
plt.title('  GPU Phase Computational Time (ms) ', fontsize =12, color='blue' )
#plt.xlabel( 'Sweeps #', fontsize = 12, color='black')
plt.ylabel(' Tiime  (ms)', fontsize = 12,color='black')
plt.ylim((10,70))
#plt.savefig('C:\LogFile\GPU Phase Computational Time ',dpi=125)      

##  Phase Computational Time for Chunk (ms)

plt.subplot(312)
plt.plot(y, PhaseComChunk, 'o', markersize=np.sqrt(5.), color='magenta');
plt.grid(b=True, which='major', color='k', linestyle='-',alpha=0.1)
plt.grid(b=True, which='minor', color='r', linestyle='-', alpha=0.1)
plt.minorticks_on()   
plt.title(' Phase Computational Time for Chunk (ms) ', fontsize =12, color='blue' )
#plt.xlabel( 'Sweeps #', fontsize = 12, color='black')
plt.ylabel(' Tiime  (ms)', fontsize = 12,color='black')
plt.ylim((50,1200))
#plt.savefig('C:\LogFile\Phase Computational Time for Chunk',dpi=125)           

## Written Disk Time (ms) 

plt.subplot(313)
plt.plot(z, DiskTime, 'o',markersize=np.sqrt(5.), color='blue');
plt.grid(b=True, which='major', color='k', linestyle='-',alpha=0.1)
plt.grid(b=True, which='minor', color='r', linestyle='-', alpha=0.1)
plt.minorticks_on()   
plt.title('  Written Disk Time (ms) ', fontsize =12, color='blue' )
#plt.xlabel( 'Sweeps #', fontsize = 12, color='black')
plt.ylabel('Time (ms)', fontsize = 12,color='black')
plt.ylim((70,1200))    
  
  
figure=plt.gcf()
figure.set_size_inches(10,10)
plt.savefig('C:\LogFile\PerformanceTest\Weight-Variance\Run_IQ\PLOT1 ',dpi=125)

plt.show ()



 # Log Metrics { Minimum, Maximum, and Average No# } 

MinGPUTime=min(GPUPhase [1:])
MaxGPUTime = max(GPUPhase [1:])
AvgGPUTime = sum(GPUPhase [1:])/len(GPUPhase [1:])

 
MinPhaseComChunk = min(PhaseComChunk[1:])
MaxPhaseComChunk= max(PhaseComChunk[1:])
AvgPhaseComChunk = sum(PhaseComChunk[1:])/len(PhaseComChunk[1:])


MinDiskTime = min(DiskTime[1:])
MaxDiskTime= max(DiskTime[1:])
AvgDiskTime= sum(DiskTime[1:])/len(DiskTime[1:])

print('\n', "Performance Report [ Pulse Rate:- 10 kHz, Start Channel =1, End Channel =9728, File Format :- BIN, Data Format :- Delta Phase,  Weight Scheme = IQ ] :- ")

print( "       "        " GPU Phase Computation Time (ms)"   "    "        "Phase Computation time for Chunk  (ms)" "    "  "Written to Disk Time (ms)", '\n'
     "Minimum =",        MinGPUTime, "                              ",  MinPhaseComChunk, "                              ", MinDiskTime, '\n'
      "Maximum =",        MaxGPUTime, "                              ",  MaxPhaseComChunk,  "                            ",   MaxDiskTime, '\n'
     "Average =",        round(AvgGPUTime,3), "                             ",  round(AvgPhaseComChunk,3),  "                            ",  round(AvgDiskTime,3))



##### 


#print('\n', "Performance Report :- ")

#print(" The Average GPU Phase Computation Time (ms) :- ", round(AvgGPUTime,3))
#print(" The Average Phase Computation time for Chunk (ms) :- ",round(AvgPhaseComChunk,3))
#print(" The Average Written to Disk Time (ms) :- ", round(AvgDiskTime,3))

#print(" The Minimum GPU Phase Computation Time (ms) :- ", round(MinGPUTime,3))
#print(" The Minimum Phase Computation time for Chunk (ms) :- ",round(MinPhaseComChunk,3))
#print(" The Minimum Written to Disk Time (ms) :- ", round(MinDiskTime,3))


#print(" The Maximum GPU Phase Computation Time (ms) :- ", round(MaxGPUTime,3))
#print(" The Maximum Phase Computation time for Chunk (ms) :- ",round(MaxPhaseComChunk,3))
#