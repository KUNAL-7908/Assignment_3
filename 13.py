# Question 13
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram

np.random.seed(42)  # For reproducibility
cols_1_to_4 = np.random.uniform(-10, 10, size=(500, 4))
cols_5_to_8 = np.random.uniform(10, 20, size=(500, 4))
cols_9_to_10 = np.random.uniform(-100, 100, size=(500, 2))
dataset = np.hstack((cols_1_to_4, cols_5_to_8, cols_9_to_10))
df = pd.DataFrame(dataset, columns=[f'col{i}' for i in range(1, 11)])

#Applying K-Means clustering
distortions = []
K = range(1, 11)  
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df)
    distortions.append(kmeans.inertia_)

plt.plot(K, distortions, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Distortion')
plt.title('K-Means Elbow Method')
plt.show()

optimal_k = 4  

kmeans = KMeans(n_clusters=optimal_k, random_state=42)
df['K Means_Cluster'] = kmeans.fit_predict(df)

# Applying Hierarchical clustering
plt.figure(figsize=(10, 7))
dendrogram_ = dendrogram(
    AgglomerativeClustering(distance_threshold=0, n_clusters=None).fit(df).linkage_,
    truncate_mode='level',
    p=5
)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel("Number of points in node (or index of point if no parenthesis).")
plt.show()

optimal_hierarchical_k = 4 
hierarchical_clustering = AgglomerativeClustering(n_clusters=optimal_hierarchical_k)
df['Hierarchical_Cluster'] = hierarchical_clustering.fit_predict(df)

print(df.head())