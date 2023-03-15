import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# Generate some random data
rng = np.random.RandomState(0)
X = rng.randn(200, 2)

# Introduce some anomalies
X[:20] += 4*np.ones((20, 2))
X[20:40] += np.ones((20, 2))

# Fit One-Class SVM
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(X)

# Predict anomalies
y_pred = clf.predict(X)

# Plot data points and anomalies
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("One-Class SVM Anomaly Detection")
plt.show()

# plot shows the normal data points in blue and the anomalies in orange