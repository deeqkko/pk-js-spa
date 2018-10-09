"""Enter initial velocity, acceleration and time (float values)
Output is a position on a second basis related to initial position and a final
final position (float values, 3 digit precision)"""


def parseInput(userInput):
    """Returns float type value"""
    try:
        return float(userInput)
    except ValueError:
        return False

def askUserInput(quizString):
    """Exits only with numeric input and returns a float type value"""
    while True:
        userInput = input(quizString)
        if parseInput(userInput) != False:
            return float(userInput)
        else:
            print("Invalid input")

def position(v0, a, t):
    """Returns position on any given time based on initial velocity
    and acceleration"""
    return v0 * t + 0.5 * a * t**2

def main():
    v0 = askUserInput("Enter initial velocity (m/s): ")
    a = askUserInput("Enter acceleration value (m/s^2): ")
    t = int(askUserInput("Enter time (s): "))
    for i in range(0, t+1):
        print(round((position(v0, a, i)),3), "m @", i,"s")


if __name__ == '__main__':
    main()
