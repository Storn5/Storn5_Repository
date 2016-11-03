def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Spam(divideBy) received 0 as argument. Can\'t divide by 0.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
