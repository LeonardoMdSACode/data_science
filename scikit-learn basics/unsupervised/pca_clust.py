from sklearn.datasets import make_blobs
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Generate sample data
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Create a PCA object with 2 components, want to reduce the dimensionality of the data to 2 dimensions
pca = PCA(n_components=2)

# Apply PCA to the data
X_pca = pca.fit_transform(X)

# Visualize the transformed data by plotting it with matplotlib
plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.show()

# creates a scatter plot of the transformed data. It uses the first component of X_pca (stored in X_pca[:, 0]) as the x-axis and the second component (stored in X_pca[:, 1]) as the y-axis.