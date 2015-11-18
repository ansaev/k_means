__author__ = 'ansaev'
from distributor import Distributor
from model import Point


class Kmeans(Distributor):

    def __init__(self, points, centroid_num):
        self.max_iterations = 4
        self.min_changes = 3
        self.centroid_num = centroid_num
        self.points = points
        self.centroids = [Point(dim=self.points[i].dim, set_id=i, cords=self.points[i].cords) for i in range(self.centroid_num)]
        # print('centroids')
        # for point in self.centroids:
        #     point.print()
        self.distr_points()

    def distribute(self):
        print('cluster learn:')
        channges = 0
        for i in range(self.max_iterations):
            channges = 0
            # print('step ' + str(i))
            self.calc_centr()
            channges = self.distr_points()
            # print('now we have:')
            # for point in self.points:
            #     point.print()
            if channges < self.min_changes:
                print('quit on step: ' + str(i) + " cause have got only " + str(channges) + " changes")
                break
        print('done all %d steps, last changes: %d' %(self.max_iterations, channges))
        return

    def calc_centr(self):
        # print('callculate new cnetr')
        for centr in self.centroids:
            points_num = 0
            cords = [0 for i in range(centr.dim)]
            for point in self.points:
                if point.distributed_set_id == centr.set_id:
                    points_num += 1
                    for i in range(centr.dim):
                        cords[i] += point.cords[i]
            if points_num is not 0:
                for i in range(centr.dim):
                    cords[i] /= points_num
            centr.cords = cords
            # centr.print()

    def distr_points(self):
        # distribute points
        changes = 0
        for point in self.points:
            distance = 99999
            for centr in self.centroids:
                my_distance = centr.dif(point)
                if my_distance < distance:
                    changes += 1
                    distance = my_distance
                    point.distributed_set_id = centr.set_id
        return changes

    def check(self):
        # learn which claster is representation of witch set
        set_hash = {}
        for set_id in range(self.centroid_num):
            cluster_points = [0 for i in range(self.centroid_num)]
            for point in self.points:
                if point.set_id == set_id:
                    cluster_points[point.distributed_set_id] += 1
            max_cluster_id = 0
            max_value = cluster_points[max_cluster_id]
            for i in range(self.centroid_num):
                if cluster_points[i] > max_value:
                    max_value = cluster_points[i]
                    max_cluster_id = i
            set_hash[set_id] = max_cluster_id

        error = 0
        for point in self.points:
            if set_hash[point.set_id] is not point.distributed_set_id:
                error += 1
        error /= len(self.points)
        print('error is: ', error)
        return error

