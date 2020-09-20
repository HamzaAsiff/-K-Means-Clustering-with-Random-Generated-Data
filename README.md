# -K-Means-Clustering-with-Random-Generated-Data

Task: Apply K-means algorithm on set of 200 datapoints to generate 2 assigned clusters

Step 1: Import following libraries:
		Numpy: To create 2d Numpy arrays of datapoints and implement K-means algo
Matplotlib: To create scatter plots for a graphical visualization of K-means clustering.

Step 2: Define a function to compute the Euclidean Distance of datapoints and their centroids.
This function will be used to update centroids, assign centroids to datapoints, get new centroids after every iteration.
	Numpy function np.linalg.norm will be used to calculate the Euclidean Distance.

Step 3: Generate two numpy arrays of 200 values. These values of these arrays will be the X and Y coordinates of the datapoints on the 2D plane.
Numpy function np.random.ranint will be used for this. Function parameters will be the start and end points and total number of points.

Step 4: Compute two random Centroids from the data. Same function will be used for this as in step 3.

Step 5: Declare two numpy arrays, one to keep the old centroids after every loop iteration and one array to keep all datapoints with their assigned cluster number

Step 6: Check for the Euclidean Distance between the old centroid and the current centroid, If the distance is greater then zero then there is need for further clustering else your algorithm has reached the global minimum.

Step 7: Compute the Euclidean Distance of the datapoints and the centroids.
Get the index of the smaller element of the array also known as the minimum distanced centroid of a point (x) in dataset
	Assign the current datapoint in the cluster array the centroid from clust2
	

Step 8: Update the location of old centroid with the current centroid
	Loop over all the data points and take average of all of them
        	which are assigned to that specific cluster

Step 9: Plot the datapoints on a scatter plot
	Take two random centroids from the datapoints
	Assign the datapoints to the clusters
Use plt.subplots to stack two scatter plots on top of each other
