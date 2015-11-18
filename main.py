__author__ = 'ansaev'

from model import Point,Points
from kmeans import Kmeans

point_dim = 2
points_num = 10
centroids_num = 5
# points = [Point(dim=point_dim, set_id=i) for i in range(points_num)]
points = Points()
points.init(file_name="separated_sets.xls")
# for point in points.points:
#     point.print()

kmeans = Kmeans(points=points.points, centroid_num=centroids_num)
kmeans.distribute()
kmeans.check()

