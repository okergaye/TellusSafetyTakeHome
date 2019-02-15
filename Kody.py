
# Osama Kergaye
# 2/15/2019
# The input will consist of a series of pairs of integers i and j,
#  one pair of integers per line.
#  All integers will be less than 1,000,000 and greater than 0.


# check the alg against every number between low and high
# import numpy as np
# import time

algCount = 0
# dynamicProgrammingQuestion = {0: 0}


def main():
   # start = time.perf_counter()
    file = open('input.txt', 'r')
    for pairs in file:
        x, y = pairs.split()
        val = kodyIsAwesome(int(x), int(y))
        print(x + " " + y + " " + str(val))
    file.close()
    #stop = time.perf_counter()

    # print(stop-start)
    return


def kodyIsAwesome(low, high):
    maxCycle = 0
    temp = 0
    global algCount
    for n in range(low, high):
        algCount = 0
        temp = algorithm(n)
        if temp > maxCycle:
            maxCycle = temp

    return maxCycle


def algorithm(n):
    global algCount
    algCount += 1

    if n == 1:
        return algCount
    elif n % 2 == 1:
        n = n*3 + 1
    else:
        n = n/2

    return algorithm(n)


if __name__ == '__main__':
    main()
