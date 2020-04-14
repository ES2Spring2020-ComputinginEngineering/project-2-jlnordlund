This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).

All nearest neighbor and k nearest neighbor functions are located in 
      NearestNeighborClassification.py 
along with the main driver. Running the code will prompt the user for a k value. After entering the k value, two graphs will appear: scatter of data from file and scatter of data with test case. The program will also print the nearest neighbor classification and k nearest neighbor classification of the test point.

The k means value classification is separated into two documents with the functions in KMeansClustering_functions.py and KMeansClustering_driver.py. Running the driver will prompt the user for a k value. This wil result in the program printing the centroids with their glucose and hemoglobin values. It will then graph the data along with the centroids. Finally, it will print out the statistics of the analysis (although, it is important to note that these values will only make sense when k = 1). The functions included in this program can be found below.

functions
  - getRandomCentroids(k,glucose,hemoglobin)
    # purpose:    returns k random points in the given data set
    # parameters: glucose array, hemoglobin array, k value
    # return:     2 arrays of length k (glucose and hemoglobin values for centroids)
  - assignClassification(glucose,hemoglobin,centroid_g,centroid_h)
    # purpose:    determines the classification of each point in the data set 
    #             based on the closest centroid
    # parameters: glucose array, hemoglobin array, 2 centroid arrays
    # return:     array of classifications (0 thru k)
  - distance(g,h,centroid_g,centroid_h)
    # purpose:    calculates the distances between a given point and all centroids
    # parameters: glucose value, hemoglobin value, centroid glucose array, centroid hemoglobin array
    # return:     array of distances
  - updateCentroids(glucose,hemoglobin,classification,k)
    # purpose:    determines new centroids based on means of glucose and hemoglobin
    # parameters: glucose array, hemoglobin array, classification array, k value
    # return:     array of glucose values of centroids and array of hemoglobin values
  - graphingKMeans(glucose,hemoglobin,assignment,cent_g,cent_h)
    # purpose:    graphs clusters and data
    # parameters: glucose array, hemoglobin array, classification array, centroid data
    # return:     void
    #
    # this code is a modification of the code found on the spec 
