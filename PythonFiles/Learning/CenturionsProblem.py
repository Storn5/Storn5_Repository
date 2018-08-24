import random

sum, ans = random.randint(1, 1000)/100, 0
print('Sum:', sum)
for i in [0.25, 0.1, 0.05, 0.01]:
    ans += int(sum//i)
    sum = round(sum%i, 2)
print('Answer:', ans)