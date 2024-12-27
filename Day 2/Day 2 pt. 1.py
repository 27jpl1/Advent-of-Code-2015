file = open("Boxes", "r")

total = 0
for line in file:
    box = line.strip().split("x")
    lw = 2 * int(box[0]) * int(box[1])
    wh = 2 * int(box[1]) * int(box[2])
    lh = 2 * int(box[0]) * int(box[2])
    minimum = min(lw, wh, lh) // 2
    total += lw + wh + lh + minimum
print(total)
