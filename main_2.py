def check_status(xox):
    status = []
    # For used to use list comprehension
    # Range put to one since just one loop for condition checking is required
    # Below three are row wise checking
    [status.append(f"{xox[0][0]} wins") for i in range(1) if xox[0][0] == xox[0][1] and xox[0][0] == xox[0][2]]
    [status.append(f"{xox[1][0]} wins") for i in range(1) if xox[1][0] == xox[1][1] and xox[1][0] == xox[1][2]]
    [status.append(f"{xox[2][0]} wins") for i in range(1) if xox[2][0] == xox[2][1] and xox[2][0] == xox[2][2]]
    # Below 3 are column wise checking
    [status.append(f"{xox[0][0]} wins") for i in range(1) if xox[0][0] == xox[1][0] and xox[0][0] == xox[2][0]]
    [status.append(f"{xox[0][1]} wins") for i in range(1) if xox[0][1] == xox[1][1] and xox[0][1] == xox[2][1]]
    [status.append(f"{xox[0][2]} wins") for i in range(1) if xox[0][2] == xox[1][2] and xox[0][2] == xox[2][2]]
    # Below 2 are diagonal checking
    [status.append(f"{xox[0][0]} wins") for i in range(1) if xox[0][0] == xox[1][1] and xox[0][0] == xox[2][2]]
    [status.append(f"{xox[0][2]} wins") for i in range(1) if xox[0][2] == xox[1][1] and xox[0][2] == xox[2][0]]
    if 'X wins' in status or 'O wins' in status:
        return status
    for i in xox:
        for j in i:
            if j == ' ':
                return "Game not finished"
    else:
        return "Draw"


def check_impossible(xox, xox_status):
    if 'X wins' in xox_status and 'O wins' in xox_status:
        return True
    x_count = 0
    y_count = 0
    for i in xox:
        for j in i:
            if j == 'X':
                x_count += 1
            if j == "O":
                y_count += 1
    if abs(x_count - y_count) > 1:
        return True


def print_xox(xox):
    print(f"""---------
| {xox[0][0]} {xox[0][1]} {xox[0][2]} |
| {xox[1][0]} {xox[1][1]} {xox[1][2]} |
| {xox[2][0]} {xox[2][1]} {xox[2][2]} |
---------""")


xox = [[' ', ' ', ' '],
       [' ', ' ', ' '],
       [' ', ' ', ' ']]
print_xox(xox)
to_play = "X"
while True:
    try:
        x, y = input("Enter the coordinates: ").split()
    except ValueError:
        print("You should enter numbers!")
        continue
    if not x.isdigit() or not y.isdigit():
        print("You should enter numbers!")
        continue
    if int(x) not in [1, 2, 3] or int(y) not in [1, 2, 3]:
        print("Coordinates should be from 1 to 3!")
        continue
    if xox[int(x) - 1][int(y) - 1] != " ":
        print("This cell is occupied! Choose another one!")
        continue
    if to_play == "X":
        xox[int(x) - 1][int(y) - 1] = "X"
        to_play = "O"
    else:
        xox[int(x) - 1][int(y) - 1] = "O"
        to_play = "X"
    print_xox(xox)
    xox_status = check_status(xox)
    if check_impossible(xox, xox_status):
        print("Impossible")
        break
    elif xox_status == "Draw":
        print("Draw")
        break
    elif 'X wins' in xox_status or 'O wins' in xox_status:
        print(xox_status[0])
        break
