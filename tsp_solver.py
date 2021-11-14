from argparser import parser
from tsp_parser import Problem
from ant_colony import ACO
import random

if __name__ == "__main__":
    # from tsp_parser import Solution
    # from ant_colony import Tour
    # Tour(Solution.from_file("berlin52.opt.tour").tour).plot_tour(Problem.from_file("berlin52.tsp"),  "optimal")
    call_args = parser.parse_args()
    tsp_file = call_args.tsp_file
    fitness_limit = call_args.fitness_limit
    population_size = call_args.population_size
    problem = Problem.from_file(tsp_file)

    if (population_size == -1):
        population_size = 300

    if (fitness_limit == -1):
        fitness_limit = problem.dim * 2000

    output = ACO(problem, population_size, 1, 2, 0.2, fitness_limit, debug=call_args.debug, plot=call_args.plot)
    with open('solution.csv', 'w') as f:
        f.write('\n'.join(map(lambda x: str(x+1), output.tour)))   # Use 1-based index for solution
    print(output.cost)
    


