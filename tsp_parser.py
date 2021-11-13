from math import sqrt, cos, acos, pi
from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt

class Distance:
    @staticmethod
    def euc(x1, y1, x2, y2):
        x_diff = x1 - x2
        y_diff = y1 - y2
        return int(sqrt(x_diff * x_diff + y_diff * y_diff)+0.5)
    
    @staticmethod
    def att(x1, y1, x2 ,y2):
        xd = x1 - x2
        yd = y1 - y2
        r = sqrt((xd*xd+yd*yd)/10.0)
        t = int(r+0.5)
        if (t < r):
            return t+1
        else:
            return t
    
    @staticmethod
    def geo(x1, y1, x2 ,y2):
        def conv_radians(x, y):
            pi_val = 3.141592
            deg = int(x+0.5)
            m = x - deg
            lat = pi_val * (deg + m * 5 / 3 ) / 180
            deg = int(y+0.5)
            m = y - deg
            lng = pi_val * (deg + m * 5 /3 ) / 180
            return lat, lng
    
        lat1, lng1 = conv_radians(x1, y1)
        lat2, lng2 = conv_radians(x2, y2)

        rrr = 6378.388

        q1 = cos(lng1 - lng2)
        q2 = cos(lat1 - lat2)
        q3 = cos(lat1 + lat2)
        return int( rrr* acos( ((1+q1)*q2 - (1-q1)*q3)/2) + 1.0)

class Problem:
    def __init__(self, name, comment, dim, dist, coords):
        self.name = name
        self.comment = comment
        self.dim = dim
        self.dist = dist
        self.coords = coords
        assert(len(coords) == dim)
    
    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as f:
            name = f.readline().split(':')[1].strip()
            next(f)   # TYPE is fixed as TSP
            comment = f.readline().split(':')[1].strip()
            dim = int(f.readline().split(':')[1])
            distance_class = f.readline().split(':')[1].strip()
            if (distance_class == "EUC_2D"):
                distance_function = Distance.euc
            elif (distance_class == "ATT"):
                distance_function = Distance.att
            elif (distance_class == "GEO"):
                distance_function = Distance.geo
            else:
                print("No such distance")
                exit()
            while(True):
                if (f.readline().strip() == "NODE_COORD_SECTION"):
                    break
            coords = np.empty([dim, 2])
            while True:
                line = f.readline().strip()
                if (line == "EOF"):
                    break
                node, x, y = line.split()
                coords[int(node)-1] = [float(x), float(y)]
        return cls(name, comment, dim, distance_function, coords)


class Solution:
    def __init__(self, name, dim, tour):
        self.name = name
        self.dim = dim
        self.tour = tour
        assert(self.dim == len(self.tour))
    
    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as f:
            name = f.readline().split(':')[1].strip()
            next(f)                                 # type is tour
            dim = int(f.readline().split(':')[1])
            next(f)                                 # tour_section
            tour = np.empty([dim], dtype=np.int32)
            for i in range(dim):
                tour[i] = int(f.readline()) - 1     # zero-indexed
        return cls(name, dim, tour)

def estimate_cost(problem, solution):
    prev_it = iter(solution.tour)
    next_it = iter(solution.tour)
    next(next_it)
    cost = 0
    stop = False
    while True:
        n = next(next_it, None)
        if (n is None):
            stop = True
            n = solution.tour[0]
        p = next(prev_it)
        cost += problem.dist(*problem.coords[n], *problem.coords[p])
        if stop:
            break
    
    return cost
