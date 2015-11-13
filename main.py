__author__ = 'ansaev'

import random
import numpy as np
points_num = 10
point_dim = 5
cluster_num = 2
cluster1_centroid = 2
cluster2_centroid = 9
points = [[random.random() for x in range(point_dim)] for i in range(points_num)]

for point in points:
    print('point')
    print('check cluster 1')
    err = 0
    for i in range(point_dim):
        err += (point[i] - points[cluster1_centroid][i])**2
    err = err ** 0.5
    print('error', err)

print(points)

