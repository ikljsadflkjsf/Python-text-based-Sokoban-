import copy
level1 = [[4,0,0],
         [3,3,0],
         [2,0,0]]

level2 = [[2,0,3,0,0,3],
         [0,1,1,0,0,0],
         [0,0,3,3,4,3]]

level3 = [[1,0,1,0,0,0],
          [2,1,0,1,0,4]]

level4 = [[0,1,0,0,3,4],
          [0,2,1,1,1,0],
          [1,1,0,0,0,0],
          [0,1,0,0,0,0]]

level5 = [[0,0,1,0,0,4],
          [0,1,0,1,1,0],
          [0,3,1,1,0,1],
          [2,1,0,1,1,0]]
levellist = [level1, level2, level3, level4, level5]
levelnumber = 0
level = copy.deepcopy(levellist[levelnumber])
print("Available commands: up, u, right, r, down, d, left, l, undo, restart, end")
print("Level 1:")

def find_location(objectnumber):
    for row in level:
        try:
            x = row.index(objectnumber)
        except:
            pass
        else:
            y = level.index(row)
    try:
        return x, y
    except:
        return None

def mover(direction, objectnumber, pos=None):
    if direction == None:
        print("Not a valid direction!")
        return
    dx, dy = direction
    if objectnumber == 2:
        x, y = find_location(objectnumber)[0], find_location(objectnumber)[1]
    else:
        x, y = pos

    if y-dy < 0 or x+dx < 0 or y-dy >= len(level) or x+dx >= len(level[0]) or level[y-dy][x+dx] == 3:
        raise IndexError
    if level[y-dy][x+dx] == 4 and not objectnumber == 2:
        raise IndexError
    else:
        if level[y-dy][x+dx] == 1:
            try: 
                mover(direction,1,(x+dx, y-dy))
            except IndexError:
                raise IndexError
        level[y-dy][x+dx] = objectnumber
        level[y][x] = 0   

def direction_words_to_numbers(direction):
    match direction.lower():
        case "up" | "u":
            return (0,1)
        case "down" | "d":
            return (0,-1)
        case "right" | "r":
            return (1,0)
        case "left" | "l":
            return (-1,0)

def has_won():
    if find_location(4) == None:
        global level, levelnumber 
        levelnumber += 1
        level = copy.deepcopy(levellist[levelnumber])
        print("\n"*5)
        print(f"Congrats! Level {levelnumber+1}:")

def print_level(level):
    printoutput = ""
    for row in level:
        for square in row:
            if square == 0:
                printoutput += "."
            if square == 1:
                printoutput += "#"
            if square == 2:
                printoutput += "O"
            if square == 3:
                printoutput += "!"
            if square == 4:
                printoutput += "W"
        printoutput += "\n"
    print(printoutput)            

while True:
    print_level(level)
    direction = input("Direction? ")
    match direction:
        case "end":
            break
        case "undo":
            level = copy.deepcopy(old_level)
        case "restart":
            level = copy.deepcopy(levellist[levelnumber])
        case _ :        
            try:
                old_level = copy.deepcopy(level)
                mover(direction_words_to_numbers(direction), 2)
            except IndexError:
                print("Invalid move")
    has_won()

    



