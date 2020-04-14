# K Means Clustering Functions
# Project 2
# Jessica Nordlund
##############################################################################

# IMPORT STATEMENTS
##############################################################################
import numpy as np
import matplotlib.pyplot as plt
import random
import math

# CUSTOM FUNCTIONS
##############################################################################
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification


# function:   getRandomCentroids
# purpose:    returns k random points in the given data set
# parameters: glucose array, hemoglobin array, k value
# return:     2 arrays of length k (glucose and hemoglobin values for centroids)
def getRandomCentroids(k,glucose,hemoglobin):
    #arrays of glucose and hemoglobin values of the centroids 
    g_cent = np.empty([0,k])
    h_cent = np.empty([0,k])
    
    for i in range(k):
        index  = random.randrange(len(glucose))
        g_cent = np.append(g_cent,glucose[index])
        h_cent = np.append(h_cent,hemoglobin[index])
        
    return g_cent,h_cent


# function:   assignClassification
# purpose:    determines the classification of each point in the data set 
#             based on the closest centroid
# parameters: glucose array, hemoglobin array, 2 centroid arrays
# return:     array of classifications (0 thru k)
def assignClassification(glucose,hemoglobin,centroid_g,centroid_h):
    classification = np.empty([0,len(glucose)])
    for i in range(len(glucose)):
        dist_to_centroids = distance(glucose[i],hemoglobin[i],centroid_g,centroid_h)
        smallest = 0
        for j in range(1,len(dist_to_centroids)):
            if dist_to_centroids[smallest] > dist_to_centroids[j]:
                smallest = j
        classification = np.append(classification,smallest)
    
    return classification
    
    
    
# function:   distance
# purpose:    calculates the distances between a given point and all centroids
# parameters: glucose value, hemoglobin value, centroid glucose array, centroid hemoglobin array
# return:     array of distances
def distance(g,h,centroid_g,centroid_h):
    distances = np.empty([0,len(centroid_g)])
    for i in range(len(centroid_g)):
         d = math.sqrt((g-centroid_g[i])**2 + (h-centroid_h[i])**2)
         distances = np.append(distances,d)
    
    return distances


# function:   updateCentroids
# purpose:    determines new centroids based on means of glucose and hemoglobin
# parameters: glucose array, hemoglobin array, classification array, k value
# return:     array of glucose values of centroids and array of hemoglobin values
def updateCentroids(glucose,hemoglobin,classification,k):
    cent_g = np.empty([0,k])
    cent_h = np.empty([0,k])
    sum_g  = 0
    sum_h  = 0
    
    for i in range(k):
        for j in range(len(glucose)):
            if (classification[j] == i):
                sum_g = sum_g + glucose[j]
                sum_h = sum_h +hemoglobin[j]
        cent_g = np.append(cent_g,sum_g/len(glucose))
        cent_h = np.append(cent_h,sum_h/len(glucose))
        
    return cent_g,cent_h


# function:   graphingKMeans
# purpose:    graphs clusters and data
# parameters: glucose array, hemoglobin array, classification array, centroid data
# return:     void
#
# this code is a modification of the code found on the spec 
def graphingKMeans(glucose, hemoglobin, assignment, cent_g, cent_h):
    plt.figure()
    for i in range(int(assignment.max()+1)):
        rcolor = np.random.rand(3,)
        plt.plot(glucose[assignment==i],hemoglobin[assignment==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(cent_g, cent_h, "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()