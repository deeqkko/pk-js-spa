#!/usr/bin/local/python3
"""Make a function average(a) which calculates an average of a list a of numbers.
 Write if __name__=='__main__': main() and test your function with couple of different parameters"""

from statistics import median



def calcMedian(numberList):
    return median(numberList)

def main():
    numberList = [1,2,3,4,5]
    print("Median of given values ", numberList, " is ", calcMedian(numberList))
    numberList = [14,2,3,10]
    print("Median of given values ", numberList, " is ", calcMedian(numberList))


if __name__ == '__main__':
    main()
