def row_check(xox):
    output = []
    if xox[0] == xox[4] and xox[0] == xox[8]:
        output.append(f"{xox[0]} wins")
    if xox[2] == xox[4] and xox[2] == xox[6]:
        output.append(f"{xox[2]} wins")
    for i in range(0, 7, 3):
        if xox[i] == xox[i + 1] and xox[i] == xox[i + 2]:
            output.append(f"{xox[i]} wins")
    for j in range(3):
        if xox[j] == xox[j + 3] and xox[j] == xox[j + 6]:
            output.append(f"{xox[j]} wins")
    if len(output) >= 1:
        return output
    else:
        if "_" in xox:
            output.append("Game not finished")
        else:
            output.append("Draw")
        return output


xox = input("Enter cells:")
xox = list(xox)
print(f"""---------
| {xox[0]} {xox[1]} {xox[2]} |
| {xox[3]} {xox[4]} {xox[5]} |
| {xox[6]} {xox[7]} {xox[8]} |
---------""")
status = row_check(xox)
x = 0
o = 0
for i in xox:
    if i == "X":
        x += 1
    elif i == "O":
        o += 1
if abs(x - o) > 1 or (len(status) > 1):
    print("Impossible")
else:
    print(status[0])
