# global var

sings_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
char = "X"
x_won = False
o_won = False
counter_X = 0
counter_O = 0


def decision():
    if is_possible():
        if o_won is False and x_won is False and counter_X + counter_O == 9:
            return "Draw"
        elif o_won:
            return "O wins"
        elif x_won:
            return "X wins"
        elif o_won is False and x_won is False and counter_X + counter_O < 9:
            return "Game not finished"
    else:
        return "Impossible"


def is_possible():
    if counter_O - counter_X > 1 or counter_X - counter_O > 1 or (o_won and x_won):
        return False
    else:
        return True


def check_three_in_row(char_field):
    holder = [1 if x == char_field else 0 for x in sings_list]
    if all(holder[0:3]) or all(holder[3:6]) or all(holder[6:9]):
        return True
    if all(holder[0:7:3]) or all(holder[1:8:3]) or all(holder[2:9:3]):
        return True
    if all(holder[0:9:4]) or all(holder[2:7:2]):
        return True
    return False


def print_board():
    print("""
    ---------
    | {0} {1} {2} |
    | {3} {4} {5} |
    | {6} {7} {8} |
    ---------
    """.format(*sings_list))


fields = {
    13: 0,
    12: 3,
    11: 6,
    23: 1,
    22: 4,
    21: 7,
    33: 2,
    32: 5,
    31: 8
}


def enter_the_coord(coord):
    coords = "".join(coord.split(" "))
    if int(coords[0]) > 3 or int(coords[1]) > 3 or int(coords[1]) < 1 or int(coords[0]) < 1:
        print("Coordinates should be from 1 to 3!")
        return False
    if sings_list[fields[int(coords)]] in ["X", "O"]:
        print("This cell is occupied! Choose another one!")
        return False
    else:
        sings_list[fields[int(coords)]] = char
        return True


print_board()
while True:
    print("Enter the coordinates: ")
    coord = input()
    if not "".join(coord.split(" ")).isnumeric():
        print("You should enter numbers!")
        continue
    if enter_the_coord(coord):
        if char == "X":
            counter_X = sings_list.count("X")
            char = "O"
        else:
            counter_O = sings_list.count("O")
            char = "X"
    else:
        continue
    print_board()
    if counter_O + counter_X >= 5:
        x_won = check_three_in_row("X")
        o_won = check_three_in_row("O")
    if counter_O + counter_X == 9 or o_won or x_won:
        break
print(decision())
