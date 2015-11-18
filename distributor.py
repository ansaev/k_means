__author__ = 'ansaev'
from abc import ABCMeta, abstractmethod, abstractproperty


class Distributor(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def distribute(self, points):
        """disribute it in some ways"""

    @abstractmethod
    def check(self):
        """check the result the error"""






