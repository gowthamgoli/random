import numpy as np 
from scipy import ndimage 
from scipy.cluster import hierarchy 
from scipy.spatial import distance_matrix 
from matplotlib import pyplot as plt 
from sklearn import manifold, datasets 
from sklearn.cluster import AgglomerativeClustering 
from sklearn.datasets.samples_generator import make_blobs 

X2, y2 = make_blobs(n_samples=200, centers=[[2, 1], [-1, -1], [5, 3], [9, 4]], cluster_std=0.9)
plt.scatter(X2[:, 0], X2[:, 1], marker='.')

agglom = AgglomerativeClustering(n_clusters = 4, linkage = 'average')
agglom.fit(X2, y2)

plt.figure(figsize=(6,4))
x_min, x_max = np.min(X2, axis=0), np.max(X2, axis=0)

X2 = (X2 - x_min) / (x_max - x_min)
cmap = plt.cm.get_cmap("Spectral")

for i in range(X2.shape[0]):        
    plt.text(X2[i, 0], X2[i, 1], str(y2[i]),
             color=cmap(agglom.labels_[i] / 10.), 
             fontdict={'weight': 'bold', 'size': 9})


plt.xticks([])
plt.yticks([])
plt.axis('off')
plt.show()
plt.scatter(X2[:, 0], X2[:, 1], marker='.')


dist_matrix = distance_matrix(X2,X2) 
Z = hierarchy.linkage(dist_matrix, 'complete')
hierarchy.dendrogram(Z)
plt.show()