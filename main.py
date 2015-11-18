__author__ = 'ansaev'

from model import Point,Points
from kmeans import Kmeans

centroids_num = 3
# points = [Point(dim=point_dim, set_id=i) for i in range(points_num)]
points = Points()
points.init(file_name="iris.xls", start_row=0, dim=4)
# for point in points.points:
#     point.print()

kmeans = Kmeans(points=points.points, centroid_num=centroids_num)
kmeans.distribute()
kmeans.check()

