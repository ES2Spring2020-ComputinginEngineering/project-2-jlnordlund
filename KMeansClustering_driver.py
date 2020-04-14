# K Means Clustering Driver
# Project 2
# Jessica Nordlund
##############################################################################

# IMPORT STATEMENTS
##############################################################################
import KMeansClustering_functions as kmc #Use kmc to call your functions
import numpy as np

# MAIN DRIVER
##############################################################################
k = int(input('Enter k value: '))
glucose, hemoglobin, classification = kmc.openckdfile()
centroid_g, centroid_h = kmc.getRandomCentroids(k,glucose,hemoglobin)
old_class = np.empty([0,len(classification)])
new_class = classification


#iterate until classifications are unchanged
while (not np.array_equal(old_class,new_class)):
    #assign classifications
    old_class = new_class
    new_class = kmc.assignClassification(glucose,hemoglobin,centroid_g,centroid_h)

    
    #update centroids
    new_cent_g, new_cent_h = kmc.updateCentroids(glucose,hemoglobin,new_class,k)


for i in range(k):
    print('Centroid ', i+1, ' : ', int(new_cent_g[i]), int(new_cent_h[i]))
    