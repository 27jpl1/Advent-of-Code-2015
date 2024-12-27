file = open("Boxes", "r")

total = 0
boxes = []
for line in file:
    box = []
    lst = line.strip().split("x")
    for part in lst:
        box.append(int(part))
    box = sorted(box)
    total += 2 * box[0] + 2 * box[1] + box[0] * box[1] * box[2]
print(total)
