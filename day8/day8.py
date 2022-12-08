grid = []
ans2 = 0
from collections import defaultdict
scenicScores = defaultdict(int)
with open("input.txt") as f:
        for line in f:
                row = []
                for c in line.strip(): 
                        row.append(int(c))
                grid.append(row)
visible = set()
for i in range(len(grid)):
        maxSoFar = -1
        for j in range(len(grid[0])):
                if grid[i][j] > maxSoFar:
                        visible.add((i, j))
                        maxSoFar = max(maxSoFar, grid[i][j])

for j in range(len(grid[0])):
        maxSoFar = -1
        maxIndex = 0
        for i in range(len(grid)):
                if grid[i][j] > maxSoFar:
                        visible.add((i, j))
                        maxSoFar = max(maxSoFar, grid[i][j])
                        maxIndex = i
for i in range(len(grid)):
        maxSoFar = -1
        maxIndex = len(grid[0])-1
        for j in range(len(grid[0])-1, -1, -1):
                if grid[i][j] > maxSoFar:
                        visible.add((i, j))
                        maxSoFar = max(maxSoFar, grid[i][j])
                        maxIndex = j
for j in range(len(grid[0])):
        maxSoFar = -1
        maxIndex = len(grid)-1
        for i in range(len(grid[0])-1, -1, -1):
                if grid[i][j] > maxSoFar:
                        visible.add((i, j))
                        maxSoFar = max(maxSoFar, grid[i][j])
                        maxIndex= i

for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
                scenicScores[(i, j)] = 1
                for x, y in [(-1, 0), (1, 0), (0,1), (0,-1)]:
                        I = i+x
                        J = j+y
                        count = 1
                        while 0 < I < len(grid)-1 and 0 < J < len(grid[0])-1 and grid[I][J] < grid[i][j]:
                                I += x
                                J += y 
                                count += 1
                        scenicScores[(i, j)]*= count
                
for v in scenicScores.values():
        ans2 = max(ans2, v)
print(len(visible))
print(ans2)