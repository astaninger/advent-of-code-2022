ans1 = 0
ans2 = 0
with open("input.txt") as f:
    for line in f:
        first_pair, second_pair = line.split(",")
        x0, y0 = first_pair.split('-')
        x1, y1 = second_pair.split('-')
        x0 = int(x0)
        x1 = int(x1)
        y0 = int(y0)
        y1 = int(y1)
        if (x0 <= x1 and x1 <= y0 and y0 >= y1 and x0 <= y1) or (x0 >= x1 and x0 <= y1 and y0 <= y1 and x1 <= y0):
            ans1 += 1
        if x0 <= x1 <= y0 or x0 <= y1 <= y0 or x1<=x0<=y1 or x1<=y0<=y1:
            ans2 += 1
print(ans1)
print(ans2)
