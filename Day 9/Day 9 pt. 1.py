from itertools import permutations

file = open("Paths", "r")

edges = {}
for line in file:
    line = line.strip().split()
    start = line[0]
    end = line[2]
    weight = line[4]
    if start in edges.keys():
        edges[start].append((end, weight))
    else:
        edges[start] = [(end, weight)]
    if end in edges.keys():
        edges[end].append((start, weight))
    else:
        edges[end] = [(start, weight)]

cities = []
for key in edges.keys():
    cities.append(key)

possibilities = list(permutations(cities))

smallest = 10000
for possibility in possibilities:
    i = 0
    total = 0
    while i < len(possibility) - 1:
        for pair in edges[possibility[i]]:
            if pair[0] == possibility[i + 1]:
                total += int(pair[1])
        if total > smallest:
            break
        else:
            i += 1
    if total < smallest:
        smallest = total
print(smallest)
