__author__ = 'ansaev'

import random
import numpy as np
# points_num = 10
# point_dim = 5
# cluster_num = 2
# cluster1_centroid = 2
# cluster2_centroid = 9
# points = [[random.random() for x in range(point_dim)] for i in range(points_num)]
#
# for point in points:
#     print('point')
#     print('check cluster 1')
#     err = 0
#     for i in range(point_dim):
#         err += (point[i] - points[cluster1_centroid][i])**2
#     err = err ** 0.5
#     print('error', err)
#
# print(points)

#
# def cluster_points(X, mu):
#     clusters  = {}
#     for x in X:
#         bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]])) \
#                     for i in enumerate(mu)], key=lambda t:t[1])[0]
#         try:
#             clusters[bestmukey].append(x)
#         except KeyError:
#             clusters[bestmukey] = [x]
#     return clusters
#
#
# def reevaluate_centers(mu, clusters):
#     newmu = []
#     keys = sorted(clusters.keys())
#     for k in keys:
#         newmu.append(np.mean(clusters[k], axis = 0))
#     return newmu
#
#
# def has_converged(mu, oldmu):
#     return (set([tuple(a) for a in mu]) == set([tuple(a) for a in oldmu]))
#
#
# def find_centers(X, K):
#     # Initialize to K random centers
#     oldmu = random.sample(X, K)
#     mu = random.sample(X, K)
#     clusters = None
#     while not has_converged(mu, oldmu):
#         oldmu = mu
#         # Assign all points in X to clusters
#         clusters = cluster_points(X, mu)
#         # Reevaluate centers
#         mu = reevaluate_centers(oldmu, clusters)
#     return(mu, clusters)
#
#
# def init_board(N):
#     X = np.array([(random.uniform(-1, 1), random.uniform(-1, 1)) for i in range(N)])
#     return X
#
#
# def init_board_gauss(N, k):
#     n = float(N)/k
#     X = []
#     for i in range(k):
#         c = (random.uniform(-1, 1), random.uniform(-1, 1))
#         s = random.uniform(0.05,0.5)
#         x = []
#         while len(x) < n:
#             a, b = np.array([np.random.normal(c[0], s), np.random.normal(c[1], s)])
#             # Continue drawing points from the distribution in the range [-1,1]
#             if abs(a) < 1 and abs(b) < 1:
#                 x.append([a,b])
#         X.extend(x)
#     X = np.array(X)[:N]
#     return X
#
# points = init_board(100)
# find_centers(points,3)
import Pycluster


