import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import make_blobs

# Generate sample data, generates a 2D dataset with three clusters
X, y = make_blobs(n_samples=50, centers=3, cluster_std=0.60, random_state=0)

# Compute the pairwise distances between the samples
distances = linkage(X, method='ward')

# Plot the dendrogram
plt.figure(figsize=(10, 7))
plt.title("Dendrogram")
dendrogram(distances)
plt.show()

#  The dendrogram shows the hierarchical relationships between the clusters, with the height of each branch representing the distance between clusters. We can use this information to determine the optimal number of clusters to use in our analysis.