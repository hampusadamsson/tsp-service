import random

import math
from copy import deepcopy

from src.Configuration import Configuration
from src.game.tsp.tsp import Tsp


class Solver:
    def __init__(self, epoch=1000):
        self.max_epoch = epoch

    def check_temp(self, i):
        if random.randint(0, self.max_epoch) > (self.max_epoch/i)*(i-1)-1:
            return True
        return False

    def run(self):
        tsp = Tsp(Configuration().problem)
        c = tsp.solution
        record = tsp.distance(c)
        total_record = record
        best_path = None
        for i in range(1, self.max_epoch):
            c1 = random.randint(0, len(c)-1)
            c2 = random.randint(0, len(c)-1)
            t = c[c1]
            c[c1] = c[c2]
            c[c2] = t
            d = tsp.distance(c)
            if d < record or self.check_temp(i):
                if d < total_record:
                    total_record = d
                    best_path = deepcopy(c)
                record = d
            else:
                t = c[c1]
                c[c1] = c[c2]
                c[c2] = t
        return total_record, best_path


"""
s = Solver()
print(s.run())

print(record)
print(total_record)
print(best_path)

record = list(map(int, "1 14 13 12 7 6 15 5 11 9 10 16 3 2 4 8".split()))
print(record)
d = tsp.distance(record)
print(d)

dd = [4, 2, 3, 1, 16, 12, 13, 14, 6, 7, 10, 9, 11, 5, 15, 8]
d = tsp.distance(dd)
print(d)
"""