import random
import sys


def randomiseMoves(path):
    # Function that accepts a incompleted path then randomises the remaining directions replacing ? in the string
    directions = "udrl"
    question_count = path.count("?")
    random_directions = []
    path = list(path)
    for i in range(question_count):
        # Randomly pick a direction
        pick = random.randint(0, 3)
        new_direction = directions[pick]
        # Add selection to list
        random_directions.append(new_direction)
    index = 0
    for i in range(len(path)):
        # Replaces ? with a direction
        if path[i] == "?":
            path[i] = random_directions[index]
            index += 1
    # Formats path back into string
    path = "".join(path)
    return path


def collisionCheck(target, maze, index, path_length):
    # Function which is given a target coordinate, the grid, the current direction index, and how many directions there are in the given path. 
    x, y = target
    # Checks whether the new position is out of bounds of the 5x5 grid
    if x < 0 or x > 4 or y < 0 or y > 4:
        return True
    # Checks whether the new position has already been used
    elif maze[y][x] == "!":
        return True
    # Checks whether the new position is the endpoint and if the character is on their last turn
    elif maze[y][x] == "G" and index != path_length - 1:
        return True
    return False


def move(direction, coordinates, maze, index, path_length):
    # Function is given a direction, the current position of the character, the grid, the current direction index,
    # and how many directions there are in the given path.
    x, y = coordinates
    # changes coordinates depending on direction
    if direction == "u":
        y -= 1
    elif direction == "d":
        y += 1
    elif direction == "r":
        x += 1
    elif direction == "l":
        x -= 1
    # Error checking
    else:
        print("Error: Invalid Input!")
    # Checks if new position causes the character to collide with anything
    if not collisionCheck([x, y], maze, index, path_length):
        # Returns coordinates of new position
        return [x, y]
    else:
        # Returns old coordinates as a way to show that something went wrong
        return coordinates


def tracePath(coordinates, maze):
    # Function that draws a ! on the new position on the grid
    x, y = coordinates
    maze[y][x] = "!"
    return maze


def printMaze(maze):
    # Displays the grid
    for row in maze:
        print("{} {} {} {} {}".format(row[0], row[1],
                                      row[2], row[3], row[4]))
    print()


def CorrectPath(path, tries):
    # Main algorithm function
    # checks if the given path is a valid path
    if not validPath(path):
        return "Invalid path"
    Found = False
    count = 1
    flag = "Found a solution!"
    # A loop that continuously attempts new random possible solutions to the incomplete path
    while not Found:
        # Reset the grid
        maze = [
                ["!", 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, "G"]
               ]
        # Initial position
        coordinates = [0, 0]
        # Randomise solution
        path = randomiseMoves(path)
        # Move the character through grid given the random path solution
        for index, direction in enumerate(path):
            coord = move(direction, coordinates, maze, index, len(path))
            if coord == coordinates:
                # Direction caused a collision, breaks for loop
                break
            else:
                # Direction was valid, setting current position to new position
                coordinates = coord
                # Draw ! on the grid at new position
                maze = tracePath(coordinates, maze)
        # If the endpoint has been travelled on by the character (only happens if character's last move causes it to land at 4, 4)
        if maze[4][4] == "!":
            # Breaks out of loop
            Found = True
        elif count > tries:
            # Amount of tries allowed is used up and no solution was found
            flag = "Likely no solution"
            break
        else:
            # Add 1 to amount of attempts used
            count += 1
    # Algorithm found no solution in the specified amount of tries
    if flag == "Likely no solution":
        return flag
    else:
        # Return the completed path, the path through the grid and the amount of attempts used to find it
        return [path, maze, count]


def display(path, maze, count, inputstring):
    # Function that prints out formatted output of given path, solution, amount of attempts and the path through the grid
    print("Given path: {}\n".format(inputstring))
    print("Completed path: {}\n".format(path))
    print("Took {} attempts to find\n".format(count))
    print("Path through grid\n")
    printMaze(maze)


def validPath(path):
    # Function that checks if the path only contains valid characters
    characters = list("udrl?")
    # Checks whether the path is a string
    if type(path) is not str:
        return False
    for direction in path:
        if direction not in characters:
            return False
    return True


# example input and output
# ???rrurdr? input
# dddrrurdrd output