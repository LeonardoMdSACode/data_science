from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generate sample data
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Create a k-means clustering model, cluster the data in 4 groups
kmeans = KMeans(n_clusters=4)

# Train the model on the data
kmeans.fit(X)

# Predict the cluster labels for the data
y_pred = kmeans.predict(X)

# Visualize the clusters
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='*', s=300, c='red')
plt.show()

# plotting the data points with their predicted labels, and also plot the cluster centers using red stars