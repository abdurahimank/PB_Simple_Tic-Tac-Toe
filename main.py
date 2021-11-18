def row_check(xox):
    output = []
    if xox[0] == "X" and xox[4] == "X" and xox[8] == "X":
        output.append("X wins")
    elif xox[0] == "O" and xox[4] == "O" and xox[8] == "O":
        output.append("O wins")
    if xox[2] == "X" and xox[4] == "X" and xox[6] == "X":
        output.append("X wins")
    elif xox[2] == "O" and xox[4] == "O" and xox[6] == "O":
        output.append("O wins")
    for i in range(0, 7, 3):
        if xox[i] == "X" and xox[i + 1] == "X" and xox[i + 2] == "X":
            output.append("X wins")
        elif xox[i] == "O" and xox[i + 1] == "O" and xox[i + 2] == "O":
            output.append("O wins")
    for j in range(3):
        if xox[j] == "X" and xox[j + 3] == "X" and xox[j + 6] == "X":
            output.append("X wins")
        elif xox[j] == "O" and xox[j + 3] == "O" and xox[j + 6] == "O":
            output.append("O wins")
    x = 0
    o = 0
    for i in xox:
        if i == "X":
            x += 1
        elif i == "O":
            o += 1
    if abs(x - o) > 1 or len(output) >= 1:
        output.append("Impossible")
        return output
    else:
        if " " in xox:
            pass  # output.append("Game not finished")
        else:
            output.append("Draw")
        return output


def play_xox(xox, player):
    coord = {(1, 1): 0, (1, 2): 1, (1, 3): 2,
             (2, 1): 3, (2, 2): 4, (2, 3): 5,
             (3, 1): 6, (3, 2): 7, (3, 3): 8}
    while True:
        x, y = input("Enter the coordinates:").split()
        num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if x not in num or y not in num:
            print("You should enter numbers!")
            continue
        elif int(x) not in [1, 2, 3] or int(y) not in [1, 2, 3]:
            print("Coordinates should be from 1 to 3!")
            continue
        else:
            if xox[coord[(int(x), int(y))]] != " ":
                print("This cell is occupied! Choose another one!")
                continue
            else:
                xox[coord[(int(x), int(y))]] = player
            break
    return xox


print(f"""---------
|       |
|       |
|       |
---------""")
xox = [" "] * 9
last = "O"
while True:
    if last == "O":
        xox = play_xox(xox, "X")
        print(f"""---------
| {xox[0]} {xox[1]} {xox[2]} |
| {xox[3]} {xox[4]} {xox[5]} |
| {xox[6]} {xox[7]} {xox[8]} |
---------""")
        last = "X"
    else:
        xox = play_xox(xox, "O")
        print(f"""---------
| {xox[0]} {xox[1]} {xox[2]} |
| {xox[3]} {xox[4]} {xox[5]} |
| {xox[6]} {xox[7]} {xox[8]} |
---------""")
        last = "O"
    status = row_check(xox)
    if ("X wins" in status) or ("O wins" in status) or ("Impossible" in status) or ("Draw" in status):
        print(status[0])
        break
    else:
        continue
