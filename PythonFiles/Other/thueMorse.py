def Main():
    str = "01"
    end = False
    while(end == False):
        strCopy = ((str.replace("0","2")).replace("1","0")).replace("2","1")
        str += strCopy
        print(str)
        if(input() == "exit"):
            end = True

if(__name__ == "__main__"):
    Main()