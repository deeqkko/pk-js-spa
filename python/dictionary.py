#!/usr/local/bin/python3

'''Make a simple dictionary application. The user can search words from the dictionary.
If the word is found, it displays the translation. if the word is not found, the program displays
"Word not found. Please input a definition".
If user submits a definition, it adds a new word to this dictionary.'''

dictionary = {}
print("""Welcome to english-finnish dictionary. Search a word typing it in english.
If word is not found you are asked to add it to dictionary with its finnish translation\n""")
while True:
    word = input("Search (l List, q Quit): ")
    if word == "q":
        print("Bye Bye!")
        quit()
    elif word == "l":
        for i in dictionary:
            print(i,"<->",dictionary[i])
    elif len(word) == 0:
        print("Enter a word...")
    else:
        try:
            print(dictionary[word])
        except KeyError:
            print("Word not found.")
            translation = input("Please input a definition (leave empty to abort): ")
            if len(translation) == 0:
                print("Aborting...")
            else:
                dictionary[word] = translation
                print("Added entry",word,"<->",translation)
