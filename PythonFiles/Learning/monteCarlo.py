# Monte Carlo algorithm for calculating area of circle
import random
import math

def calc_dist(x1, y1, x2, y2):
    return abs(math.sqrt((x1-x2)**2 + (y1-y2)**2))

total = 10_000_000
in_circle = 0

for i in range(total):
    x = random.random()
    y = random.random()
    dist = calc_dist(0.5, 0.5, x, y)
    if dist < 0.5:
        in_circle += 1

ratio = in_circle/total
print(ratio * 4)
