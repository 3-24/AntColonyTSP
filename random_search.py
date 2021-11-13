from tsp_parser import Problem
from ant_colony import ACO
import random
import argparse
import sys

parser = argparse.ArgumentParser(
      description = "Hyperparameter Optimisation through Random Search")

parser.add_argument (
      "tsp_file"
    , help    = "Path to .tsp file."
    )

if __name__ == "__main__":
    call_args = parser.parse_args()
    problem = Problem.from_file(call_args.tsp_file)
    best_cost = sys.maxsize
    best = []

    while True:
        pop_size = random.randrange(problem.dim) + 1
        alpha = random.uniform(0, 1000)
        beta = random.uniform(0, 1000)
        rate = random.uniform(0, 1)

        _, new_cost = ACO(problem, pop_size, alpha, beta, rate, problem.dim*100)

        print(f"Challenger: {(pop_size, alpha, beta, rate)}, {new_cost}")
        if (best_cost > new_cost):
            best = [(pop_size, alpha, beta, rate)]
            best_cost = new_cost
        elif (best_cost == new_cost):
            best.append((pop_size, alpha, beta, rate))
        
        print(f"{best} are best with cost {best_cost}")