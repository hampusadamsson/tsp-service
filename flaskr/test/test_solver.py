from random import Random
from unittest import TestCase

from src.Configuration import Configuration
from src.game.tsp.solver import Solver
from src.game.tsp.tsp import Tsp


class TestSolver(TestCase):
    def test_run(self):
        for t in range(1):
            s = Solver(35000)
            tsp = Tsp(Configuration().problem)
            pre_distance = tsp.distance(tsp.solution)
            post_distance, path = s.run()
#            if post_distance > 29.9:
            print(post_distance)
            print(path)
            assert pre_distance > post_distance
            tsp.solution = path
            tsp.drawUI()

    def test_run_rnd(self):
        tsp = Tsp(Configuration().problem)
        record = 999999
        for _ in range(1000000):
            rnd = Random()
            rnd.shuffle(tsp.solution)
            post_distance = tsp.distance(tsp.solution)
            if post_distance < record:
                record = post_distance
                print(post_distance)
                tsp.drawUI()
