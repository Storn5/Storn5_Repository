def revFact(n):
    f = 1
    if(n > 1):
        n = n / f
        f = f + 1
        revFact(n)
    elif(n == 1):
        return f
    elif(n < 1):
        return NULL

def Main():
    x = 120
    y = 150
    print(str(x) + "=" + str(revFact(x)) + "!")
    print(str(y) + "=" + str(revFact(y)) + "!")

if(__name__ == "__main__"):
    Main()