import random
import math


def random_string(length):
    # Generates a random bit string of the provided length
    return ''.join([random.choice(['0', '1']) for _ in range(length)])


def get_neighbors(bits):
    # bits: a bit string
    # returns a list of two bit strings with values adjacent to this bit sting.
    # If the string is zero or all ones only returns one value

    # in this case we are at the minimum value of zero
    if "1" not in bits:
        return [bits[:-1] + "1"]
    # in this case we are at the maximum value for this bit string length
    elif "0" not in bits:
        return [bits[:-1] + "0"]
    else:
        one_less = bin(int(bits, 2) - 1)[2:]
        one_greater = bin(int(bits, 2) + 1)[2:]
        return [one_less, one_greater]


def increasing_hills(x):
    # increasing hills is a fitness functions
    # x: a bit string
    # As output, the function produces an integer
    # This fitness function goes through a cosine cycle every 20 ticks
    # Getting bigger as x gets bigger
    i = int(x, 2)
    return int(i*math.cos(math.pi*i/10))


def jagged_hills(x):
    # increasing hills but with a jagged mod function to throw off
    # basic hills
    # x: a bit string
    i = int(x, 2)
    return int(i*math.cos(math.pi*i/10)) + (i % 7)

def bit_flips(x):
    # fitness function
    # counts the number of times the bits flip in the string
    # x: a bit string
    total = 0
    for i in range(len(x) - 1):
        if not x[i] == x[i+1]:
            total += 1
    return total


def mate_string(x, y):
    # Takes two strings of the same length and mates them
    # to produce a new string based on the bits of the
    # parent strings. If they have the same bit in a position
    # then the bit stays the same, otherwise it is randomly chosen
    assert len(x) == len(y)
    return ''.join([random.choice((x[i], y[i])) for i in range(len(x))])

def population_converged(pop):
    # Takes as input a list of string values
    # pop: A list of bit strings of equal length
    # Returns a boolean if the population is sufficiently close
    # to count as converged