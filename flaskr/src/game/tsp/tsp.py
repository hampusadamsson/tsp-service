import math

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.pyplot import style
style.use("ggplot")


class Tsp:
    cities = None
    problem = None
    solution = None

    def __init__(self, problem):
        self.cities = {}
        self.solution = []
        with open(problem, "r") as fn:
            for row in fn.readlines():
                id, name, x, y = row.split("\t")
                self.cities[id] = (x, y)
                self.solution.append(id)

    def distance(self, solution):
        self.solution = solution
        dist = 0.0
        if self.validate_solution(solution):
            for i, _ in enumerate(solution):
                c1 = self.cities[str(solution[i])]
                c2 = self.cities[str(solution[(i + 1) % len(solution)])]
                new_d = self.cdist(float(c1[0]), float(c1[1]), float(c2[0]), float(c2[1]))
                dist += new_d
            return dist*100 #scale distance
        else:
            return False

    def validate_solution(self, solution):
        if sorted([int(c) for c in solution]) == sorted([int(c) for c in self.cities.keys()]):
            return True
        return False

    def cdist(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def draw(self, show_id=False):
        X = []
        Y = []
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        for i in range(len(self.solution) + 1):
            y1, x1 = self.cities[self.solution[i % len(self.solution)]]
            if show_id:
                axis.text(float(x1), float(y1), self.solution[i % len(self.solution)])
            X.append(float(x1))
            Y.append(float(y1))
        axis.scatter(X, Y, c='b')
        axis.plot(X, Y, 'r-')
        axis.tick_params(top=False, bottom=False, left=False, right=False, labelleft=False, labelbottom=False)
        return fig


    def drawUI(self, show_id=False):
        X = []
        Y = []
        fig = plt.Figure()
        for i in range(len(self.solution) + 1):
            y1, x1 = self.cities[self.solution[i % len(self.solution)]]
            if show_id:
                plt.text(float(x1), float(y1), self.solution[i % len(self.solution)])
            X.append(float(x1))
            Y.append(float(y1))
        plt.scatter(X, Y, c='b')
        plt.plot(X, Y, 'r-')
        plt.tick_params(top=False, bottom=False, left=False, right=False, labelleft=False, labelbottom=False)
        plt.plot()
        plt.show()

# tsp = Tsp("ulysses16.tsp")
# tsp = Tsp("berlin52.tsp")
# f = tsp.distance("1 14 13 12 7 6 15 5 11 9 10 16 3 2 4 8".split())
# tsp.draw(True)
# print(tsp.solution)
# print(f)
