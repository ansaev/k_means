from distributor import Distributor
from model import Point
import numpy


class Prc(Distributor):
    def __init__(self, points):
        data = []
        for point in points:
            data.append(point.cords)
            pass
        self.var = len(data[0])
        self.records = len(data)
        self.x = numpy.array(data)

        print('x is', self.x, self.var, self.records)
        return

    def distribute(self):
        return

    def check(self):
        error = 0
        return error
