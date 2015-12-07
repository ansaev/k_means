__author__ = 'ansaev'

from model import Point,Points
from kmeans import Kmeans
from prc import Prc

# centroids_num = 3
points = Points()
points.init(file_name="iris.xls", start_row=0, dim=4)
#
# kmeans = Kmeans(points=points.points, centroid_num=centroids_num)
# kmeans.distribute()
# error = kmeans.check()
# print("error is %f%%" % (error*100))
#
# centroids_num = 5
# points = Points()
# points.init(file_name="separated_sets_norma.xls", start_row=0, dim=5)
#
# kmeans = Kmeans(points=points.points, centroid_num=centroids_num)
# kmeans.distribute()
# error = kmeans.check()
# print("error is %f%%" % (error*100))
#
#
#
# centroids_num = 5
# points = Points()
# points.init(file_name="separated_sets.xls", start_row=0, dim=5)
#
# kmeans = Kmeans(points=points.points, centroid_num=centroids_num)
# kmeans.distribute()
# error = kmeans.check()
# print("error is %f%%" % (error*100))

prc = Prc(points=points.points)
prc.distribute()
error = prc.check()
print("error is %f%%" % (error*100))

