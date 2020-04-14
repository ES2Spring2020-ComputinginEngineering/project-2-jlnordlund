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
    centroid_g, centroid_h = kmc.updateCentroids(glucose,hemoglobin,new_class,k)


for i in range(k):
    print('Centroid ', i+1, ' : ', int(centroid_g[i]), int(centroid_h[i]))
    
kmc.graphingKMeans(glucose,hemoglobin,new_class,centroid_g,centroid_h)



#statistics (only works when k = 1)
num_true_p  = 0
num_false_p = 0
num_true_n  = 0
num_false_n = 0
for i in range(len(new_class)):
    if new_class[i] == 0:
        if classification[i] == 0:
            num_true_n = num_true_n + 1
        else:
            num_false_n = num_false_n + 1
    else:
        if classification[i] == 0:
            num_false_p = num_false_p + 1
        else:
            num_true_p = num_true_p + 1

print('True Positive:',num_true_p/len(new_class))
print('False Positive:',num_false_p/len(new_class))
print('True Negative:',num_true_n/len(new_class))
print('False Negative:',num_false_n/len(new_class))
