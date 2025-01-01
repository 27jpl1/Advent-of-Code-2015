from collections import deque

file = open("Logic Gates", "r")

wires = {}
queue = deque()
for line in file:
    line = line.strip().split()
    queue.append(line)

second_queue = queue.copy()
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

new_wires = {"b": wires["a"]}
while second_queue:
    line = second_queue.popleft()
    if line[-1] == "b":
        pass
    elif line[1] == "AND":
        if line[0] in new_wires.keys() and line[2] in new_wires.keys():
            new_wires[line[-1]] = new_wires[line[0]] & new_wires[line[2]]
        elif line[0].isdigit() and line[2] in new_wires.keys():
            new_wires[line[-1]] = int(line[0]) & new_wires[line[2]]
        else:
            second_queue.append(line)
    elif line[1] == "OR":
        if line[0] in new_wires.keys() and line[2] in new_wires.keys():
            new_wires[line[-1]] = new_wires[line[0]] | new_wires[line[2]]
        else:
            second_queue.append(line)
    elif line[1] == "LSHIFT":
        if line[0] in new_wires.keys():
            new_wires[line[-1]] = new_wires[line[0]] << int(line[2])
        else:
            second_queue.append(line)
    elif line[1] == "RSHIFT":
        if line[0] in new_wires.keys():
            new_wires[line[-1]] = new_wires[line[0]] >> int(line[2])
        else:
            second_queue.append(line)
    elif line[0] == "NOT":
        if line[1] in new_wires.keys():
            new_wires[line[-1]] = ~new_wires[line[1]] & (2**16 - 1)
        else:
            second_queue.append(line)
    else:
        if line[0].isdigit():
            new_wires[line[-1]] = int(line[0])
        else:
            if line[0] in new_wires.keys():
                new_wires[line[-1]] = new_wires[line[0]]
            else:
                second_queue.append(line)

print(new_wires["a"])
