__author__ = 'ansaev'
from distributor import Distributor
from model import Point


class Kmeans(Distributor):

    def __init__(self, points, centroid_num):
        self.last_error = 0
        self.iterations_no_changes = 0
        self.max_iterations_no_changes = 20
        self.max_iterations = 60000
        self.min_error = 0.09
        self.centroid_num = centroid_num
        self.points = points
        self.centroids = [Point(dim=self.points[i].dim, set_id=i, cords=self.points[15*i].cords) for i in range(self.centroid_num)]
        self.distr_points()

    def distribute(self):
        print('cluster learn:', self.centroid_num)
        error = 1
        for i in range(self.max_iterations):
            self.calc_centr()
            self.distr_points()
            error = self.check()
            print('step %d, error is %f' % (i, error))
            print(str( self.min_error))
            if self.last_error == error:
                self.iterations_no_changes += 1
            self.last_error = error
            if error <= self.min_error:
                print("quit on step: %d cause error is only %f " % (i, error))
                break
            elif self.iterations_no_changes >= self.max_iterations_no_changes:
                print("quit on step: %d cause of %d iterations without changes, error is %f " % (i, self.iterations_no_changes, error))
                break
        else:
            print('done all %d steps, error is: %f' % (self.max_iterations, error))
        for point in self.points:
            point.print()
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
        real_set_id = {i for i in range(self.centroid_num)}
        for distrib_id in range(self.centroid_num):
            cluster_distribution = [0 for i in range(self.centroid_num)]
            for point in self.points:
                if point.distributed_set_id == distrib_id:
                    if int(point.set_id) in real_set_id:
                        cluster_distribution[int(point.set_id)] += 1
            real_id_win = cluster_distribution.index(max(cluster_distribution))
            if real_id_win not in real_set_id:
                real_id_win = real_set_id.pop()
            set_hash[real_id_win] = distrib_id
            try:
                real_set_id.remove(real_id_win)
            except KeyError:
                print('EEEEE', real_set_id, real_id_win, cluster_distribution, set_hash)
        error = 0
        for point in self.points:
            if int(set_hash[point.set_id]) != int(point.distributed_set_id):
                error += 1
        error /= len(self.points)
        print('hash is', set_hash)
        return error


