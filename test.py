def play_xox(xox):
    coord = {(1, 1): 0, (1, 2): 1, (1, 3): 2,
             (2, 1): 3, (2, 2): 4, (2, 3): 5,
             (3, 1): 6, (3, 2): 7, (3, 3): 8}
    while True:
        x, y = input("Enter the coordinates:").split()
        x = int(x)
        y = int(y)
        num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if x not in num or y not in num:
            print("You should enter numbers!")
            continue
        elif x not in [1, 2, 3] or y not in [1, 2, 3]:
            print("Coordinates should be from 1 to 3!")
            continue
        else:
            if xox[coord[(x, y)]] != "_":
                print("This cell is occupied! Choose another one!")
                continue
            else:
                xox[coord[(x, y)]] = "X"
            break
    return f"""---------
| {xox[0]} {xox[1]} {xox[2]} |
| {xox[3]} {xox[4]} {xox[5]} |
| {xox[6]} {xox[7]} {xox[8]} |
---------"""


xox = input("Enter cells:")
xox = list(xox)
print(f"""---------
| {xox[0]} {xox[1]} {xox[2]} |
| {xox[3]} {xox[4]} {xox[5]} |
| {xox[6]} {xox[7]} {xox[8]} |
---------""")

print(play_xox(xox))
