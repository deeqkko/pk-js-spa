"""Make a program, which gives a Finnish lottery (lotto) row.
In other words write a program which outputs 7 random numbers in ascending order
from a list of numbers from 1 to 40."""

from random import shuffle

lottery = range(0,40)
lottery = list(lottery)
shuffle(lottery)
lottery = lottery[0:8]
lottery.sort()

print("Arrrrvotaan 7 numeroa...\n",lottery)
