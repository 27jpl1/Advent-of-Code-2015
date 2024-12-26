floors = open("Floors", "r")

floor = 0
for line in floors:
    for i, char in enumerate(line.strip()):
        if char == "(":
            floor += 1
        else:
            floor -= 1
            if floor == -1:
                print(i + 1)

print(floor)
