ans = 0
with open("input.txt") as f:
    curr = 0
    totals = []
    for line in f:
        if line.strip() != "":
            curr += int(line.strip())
        else:
            ans = max(ans, curr)
            totals.append(curr)
            curr = 0


print(ans)
totals.sort()
print(sum(totals[-3:]))
