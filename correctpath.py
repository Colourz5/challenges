from correctpathrandomsearch import CorrectPath, printMaze, validPath
import sys


def main(tries):
    # Main function that continuously asks for paths, finding the solution if possible for each one
    # Default limit for amount of tries allowed to find a path
    if tries == 0:
        while True:
            givenpath = input("Enter a path: ")
            # Quits program
            if givenpath.lower() == "quit":
                print("Program has quit\n")
                break
            tries = 4**(2 * givenpath.count("?"))
            # Run pathfinding algorithm
            result = CorrectPath(givenpath, tries)
            # If function returns a list, it means it has found a solution
            if type(result) is list:
                # Unpack values
                path = result[0]
                maze = result[1]
                count = result[2]
                print("\nThis is the completed path {}\n".format(path))
                print("Took {} tries to find\n".format(count))
                printMaze(maze)
            # If function returns a string it means it encountered an error
            elif type(result) is str:
                # Algorithm used all available tries and was unable to find a solution
                if result == "Likely no solution":
                    print("There is likely no solution, as it attempted {} possible variations\n".format(tries))
                # The path the user inputted is not in the correct format
                elif result == "Invalid path":
                    print("The given path has invalid characters!\n")
    # User inputted limit of tries allowed to find a path
    else:
        while True:
            givenpath = input("Enter a path: ")
            # Quit program
            if givenpath.lower() == "quit":
                print("Program has quit\n")
                break
            # Run pathfinding algorithm
            result = CorrectPath(givenpath, tries)
            # If function returns a list, it means it has found a solution
            if type(result) is list:
                path = result[0]
                maze = result[1]
                count = result[2]
                print("\nThis is the completed path {}\n".format(path))
                print("Took {} tries to find\n".format(count))
                printMaze(maze)
            # If function returns a string it means it encountered an error
            elif type(result) is str:
                # Algorithm used all available tries and was unable to find a solution
                if result == "Likely no solution":
                    print("There is likely no solution, as it attempted {} possible variations\n".format(tries))
                # The path the user inputted is not in the correct format
                elif result == "Invalid path":
                    print("The given path has invalid characters!\n")


def avgcount():
    # Optional function that uses the default limit for tries. It asks for an amount of iterations the program should go
    # through and then averages the amount of attempts it uses to find the solution
    givenpath = input("Enter a path: ")
    tries = 4**(2 * givenpath.count("?"))
    # Loop to ensure that iterations is an integer
    while True:
        try:
            iterations = int(input("How many iterations?: "))
            break
        except ValueError:
            print("Error: Iterations must be an integer!")
    total = 0
    # Runs the CorrectPath function iterations - 1 times adding the count to total every time
    for _ in range(iterations - 1):
        result = CorrectPath(givenpath, tries)
        if result == "Likely no solution":
            print("\nNo solution to the given path!")
            sys.exit()
        count = result[2]
        total += count
    # Last iteration of the CorrectPath function
    path, maze, count = CorrectPath(givenpath, tries)
    total += count
    # Calculate the average
    average = total / iterations
    print("\nTook an average of {:.2f} attempts to solve".format(average))
    print("\nThis is the completed path {}\n".format(path))
    printMaze(maze)


def change_tries():
    # Optional function that allows user to determine the amount of tries allowed for the CorrectPath function
    # Loop to ensure input is valid
    while True:
        tries = input("Enter the amount of tries: ")
        # Make the amount of tries the default amount
        if tries.lower() == "default":
            tries = 0
            break
        # Allows user to quit the program prematurely
        elif tries.lower() == "quit":
            print("Program has quit\n")
            sys.exit()
        # Makes sure the input is non-empty
        elif tries == "":
            print("\nPlease enter a number...\n")
            continue
        # Makes sure tries is a number
        elif tries.isdigit():
            tries = int(tries)
            break
        else:
            # Checks if tries is a float
            try:
                tries = float(tries)
                break
            # Tries is not a float, looping back again to ask for input
            except ValueError:
                print("\nInvalid input!\n")
                print("\nPlease enter a number...\n")
                continue
    # Runs main with the specified tries limit
    main(tries)


if __name__ == "__main__":
    # Script's optional functions
    if len(sys.argv) == 2:
        # Gives average attempt count for a given path
        if sys.argv[1] == "--avgcount":
            avgcount()
        # Allows user to run program with different try limit
        elif sys.argv[1] == "--tries":
            change_tries()
    # Exits program if given too many arguments
    elif len(sys.argv) > 2:
        print("Too many arguments!\nPlease try again\n")
    # Runs default program function with default try limit
    else:
        main(0)
