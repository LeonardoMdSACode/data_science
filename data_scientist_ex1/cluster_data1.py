from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics.cluster import completeness_score, v_measure_score
import pickle
import numpy as np
import pytest

# You can access the `data` folder by uncommenting the following command
data = pickle.load(open("data/documents.p", "rb"))

def cluster_articles(data):
 # Extract document vectors from the data
    vectors = data["vectors"]
    
    # Perform clustering on 100-dimensional vectors
    kmeans_100 = KMeans(n_clusters=10, random_state=2, tol=0.05, max_iter=50)
    kmeans_100.fit(vectors)
    labels_100 = kmeans_100.labels_
    
    # Compute number of observations in each cluster for 100-dimensional vectors
    nobs_100 = [sum(labels_100 == i) for i in range(10)]
    
    # Reduce dimensionality of vectors using PCA
    pca = PCA(n_components=10, random_state=2)
    vectors_10 = pca.fit_transform(vectors)
    
    # Perform clustering on 10-dimensional vectors
    kmeans_10 = KMeans(n_clusters=10, random_state=2, tol=0.05, max_iter=50)
    kmeans_10.fit(vectors_10)
    labels_10 = kmeans_10.labels_
    
    # Compute number of observations in each cluster for 10-dimensional vectors
    nobs_10 = [sum(labels_10 == i) for i in range(10)]
    
    # Compute variance explained by the first component of PCA
    pca_explained = pca.explained_variance_ratio_[0]
    
    # Compute completeness score for clustering with 100-dimensional vectors
    cs_100 = completeness_score(data["group"], labels_100)
    
    # Compute completeness score for clustering with 10-dimensional vectors
    cs_10 = completeness_score(data["group"], labels_10)
    
    # Compute V-measure score for clustering with 100-dimensional vectors
    vms_100 = v_measure_score(data["group"], labels_100)
    
    # Compute V-measure score for clustering with 10-dimensional vectors
    vms_10 = v_measure_score(data["group"], labels_10)
    
    # Return a dictionary containing the computed metrics
    results = {
        "nobs_100": nobs_100,
        "nobs_10": nobs_10,
        "pca_explained": pca_explained,
        "cs_100": cs_100,
        "cs_10": cs_10,
        "vms_100": vms_100,
        "vms_10": vms_10,
    }
    return results