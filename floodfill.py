import random

def create_field(width, height):
    return [["_" for i in range(width)]
        for j in range(height)]

def fill_with_xs(count, field):
    for _ in range(count):
        while True:
            x = random.randrange(len(field[0]))
            y = random.randrange(len(field))
            if field[y][x] == "_":
                field[y][x] = "x"
                break

def print_field(field):
    for row in field[::-1]:
        print(" ".join(row))
        print()

def floodfill(x, y, field):
    if field[y][x] == "x" or field[y][x] == "O":
        return
    field[y][x] = "O"
    coords = ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
    for (i, j) in coords:
        if i < 0 or j < 0 or i >= len(field[0]) or j >= len(field):
            continue
        floodfill(i, j, field)

if __name__ == "__main__":
    x = int(input("Enter x value: "))
    y = int(input("Enter y value: "))
    field = create_field(x,y)
    print_field(field)
    print()
    xamount = int(input("Enter the x amount (max=x*y): "))
    if(xamount > x*y):
        print("Too many x")
    else:    
        fill_with_xs(xamount, field)
        print_field(field)
        print()
        placeX = int(input("Enter x coordinate for hit (0 - {}): ".format(x-1)))
        if(placeX > x-1):
            print("Can't hit further than in x-axel")
        else:
            placeY = int(input("Enter y coordinate for hit (0 - {}): ".format(y-1)))
            if(placeY > y-1):
                print("Can't hit further than in y-axel")
            else:
                floodfill(placeX, placeY, field)
                print_field(field)