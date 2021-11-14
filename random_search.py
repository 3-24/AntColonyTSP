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

    while True:
        pop_size = random.randrange(1000)+1
        alpha = 1
        beta = 2
        rate = random.uniform(0, 1)
        new_hyps = (pop_size, alpha, beta, rate)
        output = ACO(problem, *new_hyps, problem.dim*1000)

        print(f"Challenger: {new_hyps}, {output.cost}")

        if (best_cost > output.cost):
            best = new_hyps
            best_cost = output.cost
            best_fitness_count = otuput.fitness_count
        elif (best_cost == new_cost):
            if (best_fitness_count > output.fitness_count):
                best = new_hyps
        
        print(f"{best} are best with cost {best_cost}")