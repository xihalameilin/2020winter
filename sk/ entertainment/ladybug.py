from matplotlib.image import imread
import matplotlib.pyplot as plt
import os
from sklearn.cluster import KMeans
image = imread(os.path.join("ladybug.jpg"))
plt.imshow(image)

X = image.reshape(-1, 3)
kmeans = KMeans(n_clusters=5).fit(X)
print(kmeans.cluster_centers_)
segmented_img = kmeans.cluster_centers_[kmeans.labels_]
segmented_img = segmented_img.reshape(image.shape)

plt.imshow(segmented_img.astype('uint8')) # 显示图片
plt.axis('off') # 不显示坐标轴
plt.show()