from sklearn.decomposition import PCA
import numpy as np

# Generate some sample data with 100 points in 10 dimensions using numpy
X = np.random.rand(100, 10)

# Create a PCA object with 2 components
pca = PCA(n_components=2)

# Apply PCA to the data
X_pca = pca.fit_transform(X)

# Compute the reconstruction error for each point as the Euclidean distance between the original data and the reconstructed data
X_reconstructed = pca.inverse_transform(X_pca)
errors = np.linalg.norm(X - X_reconstructed, axis=1)

# Threshold the errors to identify anomalies at the 95th percentile using np.percentile
threshold = np.percentile(errors, 95)
anomalies = X[errors > threshold]

# Print the anomalies
print("Anomalies:")
print(anomalies)

# identify all points above the 95th percentile as anomalies