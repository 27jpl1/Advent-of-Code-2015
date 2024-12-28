file = open("Directions")

houses = set()
location = (0, 0)
houses.add(location)
for line in file:
    for char in line.strip():
        if char == "^":
            location = (location[0], location[1] - 1)
            houses.add(location)
        elif char == ">":
            location = (location[0] + 1, location[1])
            houses.add(location)
        elif char == "<":
            location = (location[0] - 1, location[1])
            houses.add(location)
        elif char == "v":
            location = (location[0], location[1] + 1)
            houses.add(location)
print(len(houses))
