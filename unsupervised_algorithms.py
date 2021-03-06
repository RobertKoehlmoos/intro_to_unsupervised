import random
import math


def randomized_hill_climbing(fit, get_random, get_neighbors, iterations=1):
    # This function takes as input
    # fit: A function to compute fitness of a value
    # get_random: gets a random value
    # get_neighbors: function that takes a value and returns a list of values neighboring
    # iterations: how many random restarts to perform
    # This function returns the highest value found
    assert iterations > 0

    # a random point for comparison is as good as any other
    best = get_random()
    for _ in range(iterations):
        cur = get_random()
        neighbors = get_neighbors(cur)
        # This is where the climbing happens
        while fit(best_neigh := max(neighbors, key=fit)) > fit(cur):
            cur = best_neigh
        best = max(best, cur, key=fit)
    return fit(best)


def simulated_annealing(fit, get_random, get_neighbor, init_temp=10, min_temp=0.1, alpha=0.9, iterations=1):
    # This function takes as input
    # fit: A fitness function that computes fitness for a value
    # get_random: A function that returns a random value
    # get_neighbor: A function that takes a value and returns a nearby value
    # init_temp: The initial temperature for the annealing, must be greater than 0
    # min_temp: The temperature at which the annealing algorithm will finish
    # alpha: The coefficient the temperature will be decreased by each cycle
    # iterations: how many random restarts to perform
    assert init_temp > 0
    assert min_temp > 0
    assert 1 > alpha > 0
    assert iterations > 0

    # A random initial guess for best point, just something to compare to
    best = get_random()
    for _ in range(iterations):
        # The starting point for this iteration
        cur = get_random()
        temp = init_temp
        while temp > min_temp:
            neighbor = random.choice(get_neighbor(cur))
            if fit(neighbor) >= fit(cur):
                cur = neighbor
            # The temperature based comparison for negative movement
            elif math.exp((fit(cur) - fit(neighbor)) / temp) > random.random():
                cur = neighbor
            if fit(cur) > fit(best):
                best = cur
            # Updating our temperature
            temp *= alpha
    return fit(best)


def genetic_algorithm(fit, get_random, mate, is_converged, pop_size=10, iterations=1):
    # This function takes as input
    # fit: A fitness function that computes fitness for a value
    # get_random: A function that returns a random value
    # mate: A function that takes two values and mates them to produce a new value
    # is_converged: A function that takes a list of values and returns a boolean based on if the population is converged
    # pop_size: The population size used in the genetic algorithm
    # iterations: how many random restarts to perform
    assert iterations > 0
    assert pop_size > 1

    best = get_random()
    for _ in range(iterations):
        pop = [get_random() for _ in range(pop_size)]
        cycles = 0
        while not is_converged(pop):
            top_half = sorted(pop, key=fit)[:pop_size//2]
            pop = [mate(random.choice(top_half), random.choice(top_half)) for _ in range(pop_size)]
            cycles += 1
        best = max(best, random.choice(pop), key=fit)
    return fit(best)
