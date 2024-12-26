floors = open("Floors", "r")

floor = 0
for line in floors:
    for char in line.strip():
        if char == "(":
            floor += 1
        else:
            floor -= 1

print(floor)
