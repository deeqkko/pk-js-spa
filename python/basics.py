#!/usr/local/bin/python3
"""Make a program which prints out all the integers from 100 to 0 with -2 stepping, in other words: 100, 98, 96...2, 0
-
Make a program which asks use a string and displays the first letter of that string,
the last letter of that string and length of the string. Make the program robust!
-
Make a program which asks a user how many pounds (lbs) and it converts the pounds to kilograms kg.
One pound is about is about 0.45359237 kilograms.
Make your program safe and so that it keeps asking for a valid floating point number until 1 is given.
Display the result in 2 decimal precision"""

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
