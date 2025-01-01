from collections import deque

file = open("Lights", "r")

grid = []
for i in range(0, 1000):
    row = [0] * 1000
    grid.append(row)

for line in file:
    queue = deque()
    seen = set()
    line = line.strip().split()
    if line[0] == "toggle":
        start_row, start_col = map(int, line[1].split(","))
        end_row, end_col = map(int, line[3].split(","))
        queue.append((start_row, start_col))
        while queue:
            row, col = queue.popleft()
            grid[row][col] += 2
            if row + 1 <= end_row and (row + 1, col) not in seen:
                seen.add((row + 1, col))
                queue.append((row + 1, col))
            if col + 1 <= end_col and (row, col + 1) not in seen:
                seen.add((row, col + 1))
                queue.append((row, col + 1))
    elif line[1] == "on":
        start_row, start_col = map(int, line[2].split(","))
        end_row, end_col = map(int, line[4].split(","))
        queue.append((start_row, start_col))
        while queue:
            row, col = queue.popleft()
            grid[row][col] += 1
            if row + 1 <= end_row and (row + 1, col) not in seen:
                seen.add((row + 1, col))
                queue.append((row + 1, col))
            if col + 1 <= end_col and (row, col + 1) not in seen:
                seen.add((row, col + 1))
                queue.append((row, col + 1))
    else:
        start_row, start_col = map(int, line[2].split(","))
        end_row, end_col = map(int, line[4].split(","))
        queue.append((start_row, start_col))
        while queue:
            row, col = queue.popleft()
            if grid[row][col] > 0:
                grid[row][col] -= 1
            if row + 1 <= end_row and (row + 1, col) not in seen:
                seen.add((row + 1, col))
                queue.append((row + 1, col))
            if col + 1 <= end_col and (row, col + 1) not in seen:
                seen.add((row, col + 1))
                queue.append((row, col + 1))

total = 0
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        total += grid[i][j]
print(total)
