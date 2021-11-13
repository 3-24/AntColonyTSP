from tsp_parser import Problem
from ant_colony import ACO
import random

problem = Problem.from_file("rd100.tsp")

best = (4, 144.28, 11.08, 0.5)  # 7542 berlin52
best_cost = 100000

while True:
    pop_size = max(best[0] + random.choice([1, -1]), 1)
    alpha = best[1]
    beta = best[2]
    rate = best[3]
    #alpha = best[1] * random.uniform(0.5, 1.5)
    #beta = best[2] * random.uniform(0.5, 1.5)
    #rate = max(best[3] + random.choice([0.1, -0.1]), 0)
    
    # _, cost_old = ACO(problem, pop_size, best[1], best[2], best[3], problem.dim*100)
    _, new_cost = ACO(problem, pop_size, alpha, beta, rate, problem.dim*100)

    print(f"Challenger: {(pop_size, alpha, beta, rate)}, {new_cost}")
    defended = True
    if (best_cost >= new_cost):
        best = (pop_size, alpha, beta, rate)
        best_cost = new_cost
        defended = False

    
    print(f"factor:{best[0]}, alpha:{best[1]}, beta:{best[2]}, rate:{best[3]} is best with cost {best_cost} ({'defended' if defended else 'attacked'})")
