from distributor import Distributor
from model import Point
import numpy


class Pca(Distributor):
    def __init__(self, points):
        self.var = points[0].dim
        self.records = len(points)
        data = []
        data_rev = [[] for i in range(self.var)]
        for point in points:
            data.append(point.cords)

        for point in points:
            for dim in range(self.var):
                data_rev[dim].append(point.cords[dim])

        print('data', data, 'data_rev', data_rev)
        self.x = numpy.array(data)
        self.x_rev = numpy.array(data_rev)
        print('x is', self.x, self.var, self.records)
        print('x_rev is', self.x_rev, self.var, self.records)
        return

    def distribute(self):
        self.prepare_data()
        return

    def prepare_data(self):
        avg = self.calc_avg(self.x)
        print('avg', avg)
        disper = self.calc_disper(self.x, avg)
        print('disper', disper)
        for record_id in range(self.records):
            # print('record', self.x[record_id], 'avg', avg, 'disper', disper)
            self.x[record_id] = (self.x[record_id] - avg)/disper
            print('record normalise', self.x[record_id])


        return

    def calc_avg(self, points):
        records = len(points)
        avg = [0 for i in range(self.var)]
        for record in points:
            avg += record
        avg /= [records for i in range(self.var)]
        return avg

    def calc_disper(self, points, avg):
        records = len(points)
        disper = [0 for i in range(self.var)]
        for record in points:
            disper += (record - avg)**2
        disper /= [records for i in range(self.var)]
        disper = disper ** 0.5
        return disper

    def check(self):
        error = 0
        return error
