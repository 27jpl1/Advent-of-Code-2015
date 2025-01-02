file = open("Strings", "r")

total = 0
for line in file:
    line = line.strip()
    length = len(line)
    chars = 2
    i = 0
    while i < len(line):
        char = line[i]
        if char == "\\":
            chars += 2
        elif char == "\"":
            chars += 2
        else:
            chars += 1
        i += 1
    total += chars - length

print(total)
