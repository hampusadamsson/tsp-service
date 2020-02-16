from unittest import TestCase

from src.Configuration import Configuration
from src.game.tsp.solver import Solver
from src.game.tsp.tsp import Tsp


class TestSolver(TestCase):
    def test_run(self):
        s = Solver()
        tsp = Tsp(Configuration().problem)
        pre_distance = tsp.distance(tsp.solution)
        post_distance, path = s.run()
        print(post_distance)
        assert pre_distance > post_distance
        tsp.solution = path
        tsp.drawUI()
