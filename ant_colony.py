import random
import numpy as np
from tsp_parser import Problem
import matplotlib.pyplot as plt

class Ant:
    def __init__(self, start_node, dim):
        self.dim = dim
        self.tour = np.empty([dim], dtype=int)
        self.tour[0] = start_node
        self.not_visited = np.ones(dim, dtype=bool)
        self.not_visited[start_node] = 0
        self.cost = 0
        self.tour_it = 1

    def move(self, pheromoneGraph):
        node_at = self.tour[self.tour_it-1]
        weights = np.nan_to_num(np.reshape(pheromoneGraph.pheromone_weight[node_at, :], self.dim), copy=False, nan=10000) * self.not_visited
        weights = weights / weights.sum()
        node_next = np.random.choice(self.dim, p=weights)
        self.tour[self.tour_it] = node_next
        self.tour_it += 1
        self.not_visited[node_next] = 0
        self.cost += pheromoneGraph.adj_matrix[node_at, node_next]
        if (self.tour_it == self.dim):
            self.cost += pheromoneGraph.adj_matrix[self.tour[-1], self.tour[0]]
    
    
    def reset(self):
        self.not_visited = np.ones(self.dim, dtype=bool)
        self.cost = 0
        self.tour_it = 1


class Tour:
    def __init__(self, tour):
        self.tour = tour

    def plot_tour(self, problem, index):
        for i in range(problem.dim):
            p = i
            n = (i+1) % problem.dim
            x = [problem.coords[self.tour[p], 0], problem.coords[self.tour[n], 0]]
            y = [problem.coords[self.tour[p], 1], problem.coords[self.tour[n], 1]]
            plt.plot(x, y, color='red', marker='o')
        plt.savefig(f'./outputs/tour_{index}.png')
        plt.clf()


class PheromoneGraph:
    def __init__(self, problem, a, b, evap_rate):                            # a and b are hyperparameters
        self.dim = problem.dim
        self.adj_matrix = np.zeros([self.dim, self.dim], dtype=np.int32)

        max_dist = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if (i == j):
                    self.adj_matrix[i, j] = 0
                else:
                    new_dist = problem.dist(*problem.coords[i], *problem.coords[j])
                    max_dist = max(max_dist, new_dist)
                    self.adj_matrix[i, j] = new_dist
        
        M = self.adj_matrix.copy()
        self._precalc = np.power(M / max_dist, b)

        self._pheromone = np.ones([self.dim, self.dim], dtype=np.float32)    # Set initial deposit as small amount, 1
        self.a = a
        self.b = b
        self.evap_rate = evap_rate
        self.update_total_weight()
    

    def update_total_weight(self):
        with np.errstate(divide='ignore'):
            self.pheromone_weight = np.divide(np.power(self._pheromone, self.a), self._precalc)

    def add_pheromone(self, x, y, amount):
        self._pheromone[x, y] += amount
        self._pheromone[y, x] += amount

    def evaporate(self):
        self._pheromone *= 1 - self.evap_rate
    
    def plot_pheromone(self, problem, index):
        max_pheromone = self._pheromone.max()
        for i in range(problem.dim):
            for j in range(i):
                x = [problem.coords[i, 0], problem.coords[j, 0]]
                y = [problem.coords[i, 1], problem.coords[j, 1]]
                plt.plot(x, y, alpha=self._pheromone[i, j]/max_pheromone, color='blue')
        plt.savefig(f'./outputs/pheromone_{index}.png')
        plt.clf()


def ACO(problem, population_size, a, b, evaporation_rate, fitness_limit, debug=False, plot=False):
    pheromoneGraph = PheromoneGraph(problem, a, b, evaporation_rate)
    if (debug):
        print("Pheromone graph is initialized.")
    colony = [Ant(start, problem.dim) for start in random.sample(range(problem.dim), population_size)]
    best_solution_cost = float('inf')
    finish = False
    for fitness_count in range(0, fitness_limit, population_size):
        if (plot):
            if (fitness_count % (population_size*100) == 0):
                pheromoneGraph.plot_pheromone(problem, fitness_count // (population_size*100) )
        for _ in range(problem.dim-1):
            for ant in colony:
                ant.move(pheromoneGraph)
        
        # update pheromone
        pheromoneGraph.evaporate()

        for ant in colony:
            if (ant.cost < best_solution_cost):
                best_solution = ant.tour.copy()
                best_solution_cost = ant.cost
            
            q = best_solution_cost / ant.cost
            
            prev_it = iter(ant.tour)
            next_it = iter(ant.tour)
            next(next_it)
            while (n := next(next_it, None)) is not None:
                p = next(prev_it)
                pheromoneGraph.add_pheromone(p, n, q)
            pheromoneGraph.add_pheromone(ant.tour[0], p, q)
        
        colony = [Ant(start, problem.dim) for start in random.sample(range(problem.dim), population_size)]
        
        if plot:
            if (fitness_count % (population_size*100) == 0):
                Tour(best_solution).plot_tour(problem, fitness_count // (population_size*100) )
        if debug:
            #print(best_solution_cost)
            print(f"Best cost: {best_solution_cost} ({fitness_count}/{fitness_limit})")
    
    return best_solution, best_solution_cost
