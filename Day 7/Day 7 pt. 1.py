from collections import deque

file = open("Logic Gates", "r")

wires = {}
queue = deque()
for line in file:
    line = line.strip().split()
    queue.append(line)

while queue:
    line = queue.popleft()
    if line[1] == "AND":
        if line[0] in wires.keys() and line[2] in wires.keys():
            wires[line[-1]] = wires[line[0]] & wires[line[2]]
        elif line[0].isdigit() and line[2] in wires.keys():
            wires[line[-1]] = int(line[0]) & wires[line[2]]
        else:
            queue.append(line)
    elif line[1] == "OR":
        if line[0] in wires.keys() and line[2] in wires.keys():
            wires[line[-1]] = wires[line[0]] | wires[line[2]]
        else:
            queue.append(line)
    elif line[1] == "LSHIFT":
        if line[0] in wires.keys():
            wires[line[-1]] = wires[line[0]] << int(line[2])
        else:
            queue.append(line)
    elif line[1] == "RSHIFT":
        if line[0] in wires.keys():
            wires[line[-1]] = wires[line[0]] >> int(line[2])
        else:
            queue.append(line)
    elif line[0] == "NOT":
        if line[1] in wires.keys():
            wires[line[-1]] = ~wires[line[1]] & (2**16 - 1)
        else:
            queue.append(line)
    else:
        if line[0].isdigit():
            wires[line[-1]] = int(line[0])
        else:
            if line[0] in wires.keys():
                wires[line[-1]] = wires[line[0]]
            else:
                queue.append(line)
print(wires["a"])
