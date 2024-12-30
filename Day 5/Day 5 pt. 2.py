file = open("Strings", "r")

total = 0
for line in file:
    one_in_between = False
    double_letters = False
    line = line.strip()
    for i, char in enumerate(line):
        if i + 2 < len(line) and char == line[i + 2]:
            one_in_between = True
        if i + 1 < len(line):
            double = char + line[i + 1]
            if double in line[i + 2:]:
                double_letters = True
    if one_in_between and double_letters:
        total += 1
print(total)

