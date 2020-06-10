from unsupervised_algorithms import randomized_hill_climbing, simulated_annealing, genetic_algorithm
from support_functions import *


tests = 300
hill_climbing_best = [0]
annealing_best = [0]
genetic_best = [0]

for _ in range(300):
    x = randomized_hill_climbing(increasing_hills, lambda: random_string(16), get_neighbors)
    hill_climbing_best.append(max(x, hill_climbing_best[-1]))
    x = simulated_annealing(increasing_hills, lambda: random_string(16), get_neighbors)
    annealing_best.append(max(x, annealing_best[-1]))
    x = genetic_algorithm(increasing_hills, lambda: random_string(16), mate_string, population_converged)
    genetic_best.append(max(x, annealing_best[-1]))
