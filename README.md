# pk-js-spa
UAS web-appdev training stash

Nothing fancy. Just a bunch of separate files for homework assignments.

If you REALLY find here anything worth copying do so at your own risk. If you
manage to break something or get lousy grades... "Aaawwww boohoo! Let me play
a sad song for you on the world smallest violin!"

jstutorial:

Tutorials from Mozilla tutorial page:
https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics

-----------------------------------------------------------------------------

Assignment 1:

Make a web page which has a number input field, which asks the age of the user
in years. Age must be a valid positive integer. Then you calculate the
approximate birth year of the user.

birth year = current year - age

Make user interface so that it will work on all popular devices and browsers,
including mobile. And so that it will behave nicely e.g. output an error
message, in case user gives no input or erroneous input

filename = assignment1.html

STATUS: COMPLETE
-----------------------------------------------------------------------------

Assignment 2:

Exercises for next lesson:

make a web page with 5 buttons and 1 text display with the number 0 at start
button +1 increments number by 1
button -1 decrements number by 1
button *2 multiplies number by 2
button /2 divides number by 2 and rounds down (Math.floor())
reset button resets the number to 0

filename = assignment2_1.html

UPDATE: Connected adding and subtracting to one method.
Connected multiplying and dividing to one method.
Changed reset method to work with an input argument.

STATUS: WORKING CODE

Assignment 2_2:

Strings Exercise for next lesson
make function lastCharacter(s), which always returns the last character of string s

filename = assignment2_2.js

STATUS: COMPLETE
-------------------------------------------------------------------------------
Assignment 3


Lesson #3 (Wed 29th Aug 2018)


Introduction to Regular Expressions
Regular Expressions Exercises for next lesson

make a JavaScript regular expression, which accepts any number from 1 to 9 with or without leading minus (-) e.g. suitable inputs are 1, 2, 3, -1, -9, 9 and invalid inputs are 1x, x1, 10, 0, -13

COMPLETE

make a JavaScipt regular expression, which accepts 5-digit zip codes e.g. 12345, 00000, 99999, 87665 are all valid and the following are invalid: 1234, 123456, 12345x, x12345, 667a89

COMPLETE

make a web page which has one text input field and check button. The check button verifies that the user has inputted either "yes" or "no", written in any combination of uppercase and lowercase. Thus the following are valid inputs: Yes, YES, yes, YeS, nO and the following are invalid: Yes sir, Not, EI, SI, nyet, da

COMPLETE

filename = assignment3.html

STATUS:COMPETE

Exercise #1 (difficult)

make a web page, which a form, which has a validate button and it has two password fields and code which validates that the input in both password fields is equal. The password must have 8...30 characters and can only contain the following characters: a-z, A-Z, 0-9 and .,_-

filename = passwd_validator.html

STATUS:COMPLETE

Exercise #2 (difficult)

make a web page, which has a form, with one text field and button. Pressing the button will validate that the text field input is a data of the following format day.month.year (days range from 1 to 31, months range from 1 to 12 and years range from 1000 to 9999). There can be leading zeros. For example the following dates are legal: 1.1.2000, 01.01.2000, 31.12.1999, 4.9.2017 and the following dates are invalid: 32.1.2000, 1.13.1999, 39.1.1980, 07.19.1974, 001.001.2000, 1.1.1 and 9.9.10000

filename = date.html

STATUS: COMPLETE

Exercise #3 (difficult)

make a web page, which has a form with one text field and button. Pressing the button will validate that the input is a valid Finnish id number. Also out the birthdate of the person in format day.month.year and tell the gender (male/female) See https://fi.wikipedia.org/wiki/Henkil%C3%B6tunnus

filename = ssn_validator.html

STATUS: WORKING CODE

Exercise #4 (difficult)

make a web page, which always draws 7 random numbers out of 1...40. Output should be sorted in ascending order.

filename = random.html

STATUS:COMPLETE

Exercise #5 (non greedy matching)

make a web form, which has a textarea, where you can input HTML/XML/XHTML code and a button. Pressing the button will strip out all HTML/XML/XHTML

filename = strip_tags.html

STATUS:COMPLETE

Exercise (rehearse arrays, regular expressions, functions, strings and numbers - quite difficult, but very useful)
make a web form with text area, which allows the input of multiple numbers separated by ; : , or space. Pressing a button will sum up all the numbers together

continue with above and also calculate mean (average) and median. Make separate functions without any side effects (in other words the argument to median(a) should NOT alter the argument a or any other variable.

filename = sum_mean_med.html

STATUS:COMPLETE

Exercises for next lesson

draw a simple smiley face using Canvas graphics. It could look a bit like
http://www.publicdomainpictures.net/view-image.php?image=33364

filename = smiley.html
STATUS:COMPLETE

animate a rectangle which bounces from left to right

"Turn out to be 3 balls bouncing on the canvas. Sorry about that."
filename = animballs.html
STATUS:COMPLETE

write your name on screen using canvas and gradient(s) and make it move from top to bottom

filename = myname.html
STATUS: Finally, finally COMPLETE! Wee...

make a stickman, which looks a bit like yourself using Canvas
filename = stickman.html
STATUS: COMPLETE

Make a canvas which has a stick man, which rotates around its center point (middle of torso) and a bitmap, which rotates around its middle point

filename = stickman_rotate.html
STATUS:COMPLETE

--------------------------------------------------------------------------------
<h2>Python section<h2>

"""Make a program which prints out all the integers from 100 to 0 with -2 stepping, in other words: 100, 98, 96...2, 0
-
Make a program which asks use a string and displays the first letter of that string,
the last letter of that string and length of the string. Make the program robust!
-
Make a program which asks a user how many pounds (lbs) and it converts the pounds to kilograms kg.
One pound is about is about 0.45359237 kilograms.
Make your program safe and so that it keeps asking for a valid floating point number until 1 is given.
Display the result in 2 decimal precision"""

filename = basics.py
STATUS: COMPLETE

Make a program which asks the user for initial velocity (m/s), acceleration (m/s2) and time in seconds (s). Print the position of the object calculated using the following formula. distance = v*t+0.5*a*t**2. Display the distance in meters (3 digit precision) after each second. Make the program robust.

filename = position.py
STATUS: COMPLETE

"""Make a program, which asks URL from the user.
If the URL can be opened, write the URL contents into a local file path defined by the user.
Use binary mode"""

filename = url_download.py
STATUS: COMPLETE

"""Make a program which reads a text file, which can have any number of floating point numbers, which are all in their own lines.
The program will calculate and display the sum and average (mean) of all these numbers. Make your program fool proof.
It should handle all common errors and ignore those lines of the input text file, which don't have valid numbers."""

filenames = calcFromFile.txt, calcFromFile.py
STATUS: COMPLETE
