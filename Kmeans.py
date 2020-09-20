import numpy as np
#import math
from matplotlib import pyplot as plt

iterations = 150
#Compute the Euclidean distance to find the shortest
#distance between centroid and datapoints
def computeEuclid(x, y, axis = 1):
    #dist = math.sqrt(sum([(i - j) ** 2 for i, j in zip(x, y)]))
    return np.linalg.norm(x-y, axis=axis)

#Generate 200 random data points in a 2D space
dataX = np.random.randint(-5, 10,  size = 200)
dataY = np.random.randint(-5, 10,  size = 200)
data = np.array(list(zip(dataX, dataY)))

#Compute the Centroids for the two clusters
centX = np.random.randint(-5, 10, size = 2)
centY = np.random.randint(-5, 10, size = 2)
cent = np.array(list(zip(centX, centY)))
        
#Keep the old centroids, update later
oldCent = np.zeros(cent.shape)

#Array of datapoints, after every iteration
#one datapoint will be assigned a cluster
clust1 = np.zeros(len(data))


#Check if the Euclidean Distance between old and new
#centroids is equal to zero, if yes then all datapoints have been
#pointed to their clusters
checkCluster = computeEuclid(cent, oldCent, None)

i=0
#If above answer != 0 then perfrom clustering
while checkCluster != 0 or i <= iterations:
    #Assign datapoints to centroids part
    for x in range(len(data)):
        #compute the Euclidean Distance of the datapoints and the centroids
        distEuc = computeEuclid(data[x], cent)
        #print(distEuc)
        #get the index of the smaller element of the array
        #a.k.a the minimum distanced centroid of a point (x) in dataset
        tempClust = np.argmin(distEuc)
        #assign the current datapoint in the 
        #cluster array the centroid from clust2        
        clust1[x] = tempClust
    
    #Update centroids part
    #Update the location of old centroid with the current centroid        
    oldCent = cent
    for y in range(2):
        #points = [data[j] for j in range(len(data)) if clust1[j] == y]
        #Loop over all the data points and take average of all of them
        #which are assigned to that specific cluster
        for j in range(len(data)):
            if clust1[j] == y:
                clusterPT = data[j]
        cent[y] = np.mean(clusterPT, axis = 0)
    checkCluster = computeEuclid(cent, oldCent, None)
    i+=1
    
#Plotting Part
#Plot the datapoints on a scatter plot
plt.scatter(dataX, dataY, c='black', s=7)
#Take two random centroids from the datapoints
plt.scatter(centX, centY, marker='*', c='r', s=200)
#Assign the datapoints to the clusters
#Final graph after whole clustering will be output of the below code 
colors = ['y', 'b']
#Use plt.subplots to stack two scatter plots on top of each other
fig, ax = plt.subplots()
for i in range(2):
    points = np.array([data[j] for j in range(len(data)) if clust1[j] == i])
    ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i])
    ax.scatter(cent[:, 0], cent[:, 1], marker='*', s=200, c='r')
    plt.show()
