from math import sqrt
from random import random
import numpy as np

def max_of_2(n):
    list_of_maxs = []
    for i in range(n):
        x1 = random()
        x2 = random()
        list_of_maxs.append(max([x1, x2]))
    print(f'Mean of maxes: {np.mean(list_of_maxs)}')
    print(f'Std deviation of maxes: {np.std(list_of_maxs, ddof=1)}')

def sqrt_of_1(n):
    list_of_sqrts = []
    for i in range(n):
        x1 = random()
        list_of_sqrts.append(sqrt(x1))
    print(f'Mean of sqrts: {np.mean(list_of_sqrts)}')
    print(f'Std deviation of sqrts: {np.std(list_of_sqrts, ddof=1)}')

def main():
    max_of_2(10_000)
    sqrt_of_1(10_000)

if __name__ == '__main__':
    main()

