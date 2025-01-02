file = open("Strings", "r")

total = 0
for line in file:
    line = line.strip()
    length = len(line)
    line = line[1:-1]
    chars = 0
    i = 0
    while i < len(line):
        chars += 1
        char = line[i]
        if char == "\\":
            if line[i + 1] == "\\":
                i += 2
            elif line[i + 1] == "x":
                i += 4
            elif line[i + 1] == "\"":
                i += 2
        else:
            i += 1
    total += length - chars

print(total)
