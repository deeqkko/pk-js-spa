#!/usr/bin/local/python3
"""Make a function average(a) which calculates an average of a list a of numbers.
 Write if __name__=='__main__': main() and test your function with couple of different parameters"""

from statistics import mean



def calcAverage(numberList):
    print("Average of given values: ", mean(numberList))

def main():
    numberList1 = [1,2,3,4,5,6]
    numberList2 = [34,56,102,9999]
    numberList3 = [-345,1,0,800]
    calcAverage(numberList1)
    calcAverage(numberList2)
    calcAverage(numberList3)

if __name__ == '__main__':
    main()
