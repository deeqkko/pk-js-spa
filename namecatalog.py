#!/usr/local/bin/python3

"""Make a program which asks user for names and keeps accumulating the names into a list.
If use gives empty input, display all the names in alphabetical order,
tell the number of names and how many "Jack" names your list had."""
from collections import Counter

catalog = []
while True:
    try:
        entry = input("Type a name (empty value lists names, CTRL-C quits): ")
        if len(entry) == 0:
            catalog = sorted(catalog)
            for a in catalog:
                print(a)
            print("Entries:",len(catalog))
            print(Counter(catalog))

        else:
            catalog.append(entry)
    except KeyboardInterrupt:
        print("\nHave a nice day")
        quit()
