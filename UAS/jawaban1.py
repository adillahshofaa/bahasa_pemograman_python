def printHobi(x):
    if x == 0:
        return
    else:
        print("Saya suka memasak")
        return printHobi(x-1)


printHobi(5)
