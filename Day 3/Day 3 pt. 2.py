file = open("Directions")

houses = set()
santa = (0, 0)
robo_santa = (0, 0)
houses.add(santa)
houses.add(robo_santa)
is_santa = True
for line in file:
    for char in line.strip():
        if is_santa:
            if char == "^":
                santa = (santa[0], santa[1] - 1)
                houses.add(santa)
            elif char == ">":
                santa = (santa[0] + 1, santa[1])
                houses.add(santa)
            elif char == "<":
                santa = (santa[0] - 1, santa[1])
                houses.add(santa)
            elif char == "v":
                santa = (santa[0], santa[1] + 1)
                houses.add(santa)
            is_santa = False
        else:
            if char == "^":
                robo_santa = (robo_santa[0], robo_santa[1] - 1)
                houses.add(robo_santa)
            elif char == ">":
                robo_santa = (robo_santa[0] + 1, robo_santa[1])
                houses.add(robo_santa)
            elif char == "<":
                robo_santa = (robo_santa[0] - 1, robo_santa[1])
                houses.add(robo_santa)
            elif char == "v":
                robo_santa = (robo_santa[0], robo_santa[1] + 1)
                houses.add(robo_santa)
            is_santa = True
print(len(houses))
