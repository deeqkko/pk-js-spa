#!/usr/local/bin/python3
#Testing sublime git interface

def everyOther(start = 0, stop = 0, step = 1):
    """Returns a number sequence with given range and step
    Lesson 1 - Ex 1"""
    start = list(range(start, stop))
    return start[::step]

def askString():
    """Prints first and last characters and length of given String
    Lesson 1 - Ex 2"""
    while True:
        userString = input("Give me a string: ").strip()
        if len(userString):
            print("First letter: ", userString[:1])
            print("Last letter: ", userString[-1:])
            print("String length: ", len(userString))
            return

def lbsToKg():
    """Converts given float value (lbs) to kilograms
    Lesson 1 - Ex 3"""
    while True:
        try:
            userInput = float(input("Give a weight in lbs: "))
            print(round(userInput * 0.45359237, 2), " kg")
            return
        except ValueError:
            print("Invalid value.")



def main():
    #print(everyOther(0,101, -2))
    #askString()
    lbsToKg()

if __name__ == '__main__':
    main()