__author__ = 'ansaev'

from model import Point,Points
from kmeans import Kmeans
from pca import Pca

# print('iris fishers')
# points = Points()
# points.init(file_name="iris.xls", start_row=0, dim=4)
# kmeans = Kmeans(points=points.points, centroid_num=3)
# kmeans.distribute()
# error = kmeans.check()
# print('iris fishers')
# print("error is %f%%" % (error*100))
#
# print('separated sets')
# points = Points()
# points.init(file_name="separated_sets.xls", start_row=0, dim=5)
# kmeans = Kmeans(points=points.points, centroid_num=5)
# kmeans.distribute()
# error = kmeans.check()
# print('separated sets')
# print("error is %f%%" % (error*100))
#
# print('separated sets normalize')
# points = Points()
# points.init(file_name="separated_sets_norma.xls", start_row=0, dim=5)
# kmeans = Kmeans(points=points.points, centroid_num=5)
# kmeans.distribute()
# error = kmeans.check()
# print('separated sets normalize')
# print("error is %f%%" % (error*100))
#
# print('none separated sets')
# points = Points()
# points.init(file_name="sets_connected.xls", start_row=0, dim=5)
# kmeans = Kmeans(points=points.points, centroid_num=5)
# kmeans.distribute()
# error = kmeans.check()
# print('none separated sets')
# print("error is %f%%" % (error*100))
#
# print('none separated sets normalize')
# points = Points()
# points.init(file_name="sets_connected_norma.xls", start_row=0, dim=5)
# kmeans = Kmeans(points=points.points, centroid_num=5)
# kmeans.distribute()
# error = kmeans.check()
# print('none separated sets normalize')
# print("error is %f%%" % (error*100))

points = Points()
points.init(file_name="iris.xls", start_row=0, end_row=2, dim=4)
prc = Pca(points=points.points)
prc.distribute()
error = prc.check()
print("error is %f%%" % (error*100))

