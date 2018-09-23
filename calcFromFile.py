"""Make a program which reads a text file, which can have any number of floating point numbers, which are all in their own lines.
The program will calculate and display the sum and average (mean) of all these numbers. Make your program fool proof.
It should handle all common errors and ignore those lines of the input text file, which don't have valid numbers."""

from fileinput import input as fileInput
from math import fsum
from statistics import mean
floatNumbers = []

with fileInput(files="calcFromFile.txt") as fileContent:
    for line in fileContent:
        try:
            line = float(line)
            floatNumbers.append(line)
        except ValueError:
            print("Line", fileContent.lineno(),": Not a float value. Ignoring...")
        except TypeError:
            print("Line", fileContent.lineno(),": Not a float value. Ignoring...")

print("Sum of given values: ",fsum(floatNumbers))
print("Mean of given values: ", mean(floatNumbers))
