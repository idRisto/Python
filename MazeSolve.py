import csv, os, sys, time, random

def get_maze(file):
    f = open(file, 'r')
    reader = csv.reader(f)
    maze = []
    for line in reader:
        maze.append(line)
    return maze

def display_maze(m, path):
    m2 = m[:]
    os.system('cls')

    for item in path:
        m2[item[0]][item[1]] = "."          #show . on path after "mouse"

    m2[path[-1][0]][path[-1][1]] = "€"      #show "mouse" on maze

    draw = ""                               #Make a long string from maze
    for row in m2:
        for item in row:
            item = str(item).replace("1","█")
            item = str(item).replace("0"," ")
            item = str(item).replace("2"," ")       #replace "2" to " " for visual purposes
            draw += item
        draw += "\n"                                #After each row make another row
    print(draw)

def move(path):
    time.sleep(0.1)                                 #Slow down the process
    cur = path[-1]
    
    display_maze(maze, path)
    possibles = [(cur[0],cur[1] + 1), (cur[0],cur[1] - 1), (cur[0] + 1, cur[1]), (cur[0] - 1, cur[1])]  #Check for all four directions
    random.shuffle(possibles)   #randomize the order which is checked first
    
    for item in possibles:
        if item[0] < 0 or item[1] < 0 or item[0] > len(maze) or item[1] > len(maze[0]):                 #Deny access outside the maze
            continue
        elif maze[item[0]][item[1]] in ["1","2"]:
            continue
        elif item in path:
            continue
        elif maze[item[0]][item[1]] == "E": #When exit is found
            path = path + (item,)               
            display_maze(maze,path)
            input("You've done it, press enter to finish")
            os.system('cls')
            sys.exit()
        else:                               #Move forvard where possible
            newpath = path + (item,)        #make a new path which adds new coordinates to path
            move(newpath)                   #move to new path
            maze[item[0]][item[1]] = "2"    #Add "2" to where has been visited
            display_maze(maze,path)         
            time.sleep(0.1)                 #slow down the backtracking

maze = get_maze('maze2.csv')                #Filenames are maze.csv and maze2.csv

move(((18,18),))                            #Enter the starting point here (maze = 9,18 ; maze2 = 18,18)