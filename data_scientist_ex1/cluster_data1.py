from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics.cluster import completeness_score, v_measure_score
import pickle
import numpy as np

# You can access the `data` folder by uncommenting the following command
data = pickle.load(open("data/documents.p", "rb"))

def cluster_articles(data):
    # Clustering with 100 dimensional vectors
    X = np.array(data['vectors'])
    kmeans_100 = KMeans(n_clusters=10, random_state=2, tol=0.05, max_iter=50).fit(X)
    
    # Clustering with 10 dimensional vectors after PCA
    pca = PCA(n_components=10, random_state=2)
    X_pca = pca.fit_transform(X)
    kmeans_10 = KMeans(n_clusters=10, random_state=2, tol=0.05, max_iter=50).fit(X_pca)
    
    # Completeness scores for cluster labels given true values
    cs_100 = completeness_score(data['group'], kmeans_100.labels_)
    cs_10 = completeness_score(data['group'], kmeans_10.labels_)
    
    # V-measure scores for cluster labels given true values
    vms_100 = v_measure_score(data['group'], kmeans_100.labels_)
    vms_10 = v_measure_score(data['group'], kmeans_10.labels_)
    
    # Number of observations in each cluster
    nobs_100 = pd.Series(kmeans_100.labels_).value_counts().sort_index().tolist()
    nobs_10 = pd.Series(kmeans_10.labels_).value_counts().sort_index().tolist()
    
    # Variance explained by the first component in PCA
    pca_explained = pca.explained_variance_ratio_[0]

    
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