__author__ = 'ansaev'

from model import Point,Points
from kmeans import Kmeans

centroids_num = 3
points = Points()
points.init(file_name="iris.xls", start_row=0, dim=4)

kmeans = Kmeans(points=points.points, centroid_num=centroids_num)
kmeans.distribute()
error = kmeans.check()
print("error is %f%%" % (error*100))

