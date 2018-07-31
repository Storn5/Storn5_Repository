import random

blues, reds = 0, 0
iter = int(input("Enter the number of iterations: "))
for i in range(iter):
    card = random.choice(['RR', 'RB', 'BB'])
    side = random.choice([0, 1])
    if card[side] == 'B':
        if side == 0:
            if card[1] == 'B':
                blues += 1
            elif card[1] == 'R':
                reds += 1
        else:
            if card[0] == 'R':
                reds += 1
            elif card[0] == 'B':
                blues += 1

print((blues/(reds + blues)) * 100)
input()
