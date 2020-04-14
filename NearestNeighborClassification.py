# NearestNeighborClassification
# Project 2
# Jessica Nordlund
##############################################################################

# IMPORT STATEMENTS
##############################################################################
import numpy as np
import matplotlib.pyplot as plt
import random
import math


# FUNCTIONS
##############################################################################
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification


# function:   normalizeData
# purpose:    normalizes and returns two numpy arrays of equal length
#             (classification array does not need to be normalized)
# parameters: two numpy arrays of equal length
# return:     two numpy arrays of equal length (normalized)
def normalizeData(glucose, hemoglobin):
    array_size = len(glucose)
    new_glucose = np.empty([0,array_size])
    new_hemoglobin = np.empty([0,array_size])
    
    for g in glucose:
        new_g = (g - 70) / 420
        new_glucose = np.append(new_glucose, new_g)
    
    for h in hemoglobin:
        new_h = (h - 3.1) / 14.7
        new_hemoglobin = np.append(new_hemoglobin, new_h)
        
    
    return new_glucose, new_hemoglobin

# function:   normalizePoint
# purpose:    normalizes and returns two ints
#             (classification array does not need to be normalized)
# parameters: glucose and hemoglobin ints
# return:     glucose and hemoglobin ints
def normalizePoint(glucose, hemoglobin):
    new_g = (glucose - 70) / 420
    new_h = (hemoglobin - 3.1) / 14.7
      
    
    return new_g, new_h


# function:   graphData
# purpose:    creates a scatter plot with glucose along the y axis and 
#             hemoglobin as the x axis (the different classifications are 
#             color coded)
# parameters: three numpy arrays of equal length
# return:     void
def graphData(glucose, hemoglobin, classification):
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()

# function:   createTestCase
# purpose:    creates a random test case and returns the test values of 
#             glucose and hemoglobin 
# parameters: none
# return:     two ints (newhemoglobin newglucose)
def createTestCase():
    hemo_min = 3
    hemo_max = 18
    gluc_min = 70
    gluc_max = 490
    
    return random.randrange(gluc_min,gluc_max), random.randrange(hemo_min,hemo_max)



# function:   calculateDistanceArray
# purpose:    creates a numpy array of distances between given point and 
#             every other point in the data set
# parameters: new glucose value, new hemoglobin value, array of all glucose
#             values, and array of all hemoglobin values
# return:     numpy array (of distances)    
def calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin):
    distances = np.empty([0,len(glucose)])
    for i in range(len(glucose)):
        dist = math.sqrt((newglucose-glucose[i])**2 + (newhemoglobin-hemoglobin[i])**2)
        distances = np.append(distances,dist)
            
    return distances



# function:   nearestNeighborClassifier
# purpose:    uses calculateDistArray to return the classification of the
#             given point (0 or 1) based on the nearest neighbor
# parameters: new glucose value, new hemoglobin value, array of all glucose
#             values, array of all hemoglobin values, and array of all 
#             classifications
# return:     int (classificiation)
def nearestNeighborClassifier(newglucose,newhemoglobin,glucose,hemoglobin,classification):
    distances = calculateDistanceArray(newglucose,newhemoglobin,glucose,hemoglobin)
    nearest = 0
    for i in range(1,len(distances)):
        if (distances[nearest] > distances[i]):
            nearest = i
    return classification[nearest]        


# function:   graphTestCase
# purpose:    graphs test case along with other data
# parameters: new glucose value, new hemoglobin value, array of all glucose
#             values, array of all hemoglobin values, and array of 
#             classifications
# return:     void
def graphTestCase(newglucose,newhemoglobin,glucose,hemoglobin,classifications):
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    
    plt.plot(newglucose,newhemoglobin,'bo')
    
    plt.show()
    
    
    
# function:   kNearestNeighborClassifier
# purpose:    returns classification based on k nearest neighbor
# parameters: k value, new glucose value, new hemoglobin value, array of all glucose
#             values, array of all hemoglobin values, and array of classifications
# return:     classification (0 or 1)
def kNearestNeighborClassifier(k,newglucose,newhemoglobin,glucose,hemoglobin,classification):
    k_nearest = []
    distances = calculateDistanceArray(newglucose,newhemoglobin,glucose,hemoglobin)
    for i in range(k):
        k_nearest = np.append(k_nearest,i)
    for i in range(k,len(distances)):
        for j in range(k):
            if distances[i] < distances[j]:
                k_nearest[j] = i
                break
     
    sum_class = 0           
    for i in range(k):
       index = int(k_nearest[i])
       sum_class = sum_class + classification[index]
    avg = sum_class/k
    
    if avg >= 0.5:
        return 1
    return 0

# MAIN SCRIPT
##############################################################################
glucose, hemoglobin, classification = openckdfile()
k = int(input('K value: '))

print('Graphing normalized data...')
glucose, hemoglobin = normalizeData(glucose,hemoglobin)
graphData(glucose,hemoglobin,classification)

newglucose, newhemoglobin = createTestCase()
newglucose, newhemoglobin = normalizePoint(newglucose,newhemoglobin)
newclass1 = nearestNeighborClassifier(newglucose,newhemoglobin,glucose,hemoglobin,classification)
newclass2 = kNearestNeighborClassifier(k,newglucose,newhemoglobin,glucose,hemoglobin,classification)

print('Graphing data with random test case')
graphTestCase(newglucose,newhemoglobin,glucose,hemoglobin,classification)
print('Nearest Neighbor Classification = ', newclass1)
print('K Nearest Neighbor Classification = ', newclass2)