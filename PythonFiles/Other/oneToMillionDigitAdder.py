def Main():
    sum = 0
    for i in range(1000001):
        for char in str(i):
            sum += int(char)
    print(sum)

if(__name__ == "__main__"):
    Main()