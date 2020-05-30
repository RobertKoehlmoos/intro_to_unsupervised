import matplotlib
import random
import math


def randomized_hill_climbing(fit, get_random, get_neighbors, iterations=50):
    # This function takes as input
    # fit: A function to compute fitness of a value
    # get_random: gets a random value
    # get_neighbors: function that takes a value and returns a list of values neighboring
    # iterations: how many random restarts to perform
    # This function returns the value with the highest fitness found
    assert iterations > 0

    # a random point for comparison is as good as any other
    best = get_random()
    for _ in range(iterations):
        cur = get_random()
        neighbors = get_neighbors(cur)
        # This is where the climbing happens
        while fit(best_neigh := max(neighbors, fit)) > fit(cur):
            cur = best_neigh
        best = max(best, cur, fit)
    return best


def simulated_annealing(fit, get_random, get_neighbor, init_temp=10, min_temp=0.1, alpha=0.9, iterations=50):
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
            neighbor = get_neighbor(cur)
            if fit(neighbor) > fit(cur):
                cur = neighbor
            # The temperature based comparison for negative movement
            elif math.exp(fit(cur) - fit(neighbor) / temp) > random.random():
                cur = neighbor
            if fit(cur) > fit(best):
                best = cur
            # Updating our temperature
            temp *= alpha
    return best


def genetic_algorithm(fit, get_random, mate, is_converged, pop_size=10, iterations=50):
    # This function takes as input
    # fit: A fitness function that computes fitness for a value
    # get_random: A function that returns a random value
    # mate: A function that takes two values and mates them to produce a new value
    # pop_size: The population size used in the genetic algorithm
    # iterations: how many random restarts to perform
    assert iterations > 0
    assert pop_size > 1

    best = get_random()
    for _ in range(iterations):
        pop = [get_random for _ in range(pop_size)]
        while not is_converged(pop):
            top_half = pop.sort(fit)[:len(pop)/2]
            pop = [mate(random.choice(top_half), random.choice(top_half)) for _ in range(pop_size)]
        if fit(cur_best := max(pop, fit)) > fit(best):
            best = cur_best
    return best
