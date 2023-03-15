from sklearn.cluster import KMeans
import numpy as np

# Generate some sample data with 100 points in 10 dimensions using numpy
X = np.random.rand(100, 10)

# Create a k-means clustering model
kmeans = KMeans(n_clusters=5)

# Train the model on the data
kmeans.fit(X)

# Compute the distance of each point to its nearest cluster center
distances = kmeans.transform(X)
min_distances = np.min(distances, axis=1)

# Threshold the distances to identify anomalies at the 95th percentile using np.percentile
threshold = np.percentile(min_distances, 95)
anomalies = X[min_distances > threshold]

# Print the anomalies
print("Anomalies:")
print(anomalies)

# identify any points with minimum distances above the 95th percentile as anomalies