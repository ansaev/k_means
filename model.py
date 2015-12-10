__author__ = 'ansaev'
import random
import xlrd


class Point(object):
    def __init__(self, dim, set_id, cords=None):
        self.distributed_set_id = None
        self.set_id = set_id
        self.dim = dim
        if cords is None:
            self.cords = [random.random() for i in range(self.dim)]
        else:
            if len(cords) is not self.dim:
                raise ValueError('Dim of point is ' + str(self.dim) + ", but dim of cords is " + str(len(cords)) )
            self.cords = cords

    def dif(self, point):
        distance = 0
        for i in range(self.dim):
            distance += (point.cords[i] - self.cords[i])**2
        distance = pow(distance, 0.5)
        return distance

    def print(self):
        print('point', self.cords, 'dim', self.dim, 'distributed class: ' + str(self.distributed_set_id), ', self class = ' + str(self.set_id))
        return


class Points(object):
    def __init__(self):
        self.points = []

    def init(self, file_name, sheet_num=0, start_row=1, end_row=None, start_cell=0, dim=5):
        rb = xlrd.open_workbook(file_name, formatting_info=True)
        sheet = rb.sheet_by_index(sheet_num)
        if end_row is None:
            end_row = sheet.nrows
        for row_num in range(start_row, end_row):
            row = sheet.row_values(row_num)
            point = Point(cords=row[start_cell:start_cell+dim], set_id=row[start_cell+dim], dim=dim)
            self.points.append(point)


