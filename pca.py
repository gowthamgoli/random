import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA

scaler = StandardScaler()

# get data
cancer = load_breast_cancer()

# get features and labels
X = cancer.data
y = cancer.target
color = ['orange' if label == 0 else 'blue' for label in y]
marker = ['^' if label == 0 else 'o' for label in y]

# scale features
X_scaled = scaler.fit_transform(X)

# Reduce dimensions using PCA
pca = PCA(n_components=2)
pca.fit(X_scaled)
X_pca = pca.transform(X_scaled)

# 2D plot with the first principal component as x axis and the second principal component as y axis
X_benign = X_pca[y==1]
X_malignant= X_pca[y==0]
benign = plt.scatter(X_benign[:, 0], X_benign[:, 1], c='orange', marker='^')
malignant = plt.scatter(X_malignant[:, 0], X_malignant[:, 1], c='blue', marker='o')
plt.legend((benign, malignant), ('benign', 'malignant'), loc='upper right',)
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.show()


# 3d plot of first 3 features (as x, y and z)
fig = plt.figure()
cmap = plt.cm.get_cmap("Spectral")
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=10, azim=10)
ax.scatter(X_scaled[:, 0], X_scaled[:, 1], X_scaled[:, 2], cmap=cmap, c=y.astype(np.float))
plt.title('First 3 features of scaled X')
plt.show()

# 3d plot of first 2 PCs of X after transform
fig = plt.figure()
cmap = plt.cm.get_cmap("Spectral")
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=10, azim=10)
ax.scatter(X_pca[:, 0], X_pca[:, 1], cmap=cmap, c=y.astype(np.float))
plt.title('First two principal compnents of X after PCA transformation')
plt.show()

print("Original Shape: ", X_scaled.shape)
print("Reduced Shape: ", X_pca.shape)
print("PCA component shape: ", pca.components_.shape)
print("PCA components: ", pca.components_)
