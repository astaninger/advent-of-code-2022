ans1 = 0
found1 = False
found2 = False
ans2 = 0
from collections import Counter
with open("input.txt") as f:
    line = f.readlines()[0].strip()
    curr = Counter()
    currSet = set()
    curr2 = Counter()
    currSet2 = set()
    for i in range(len(line)):
        if len(currSet) == 4 and not found1:
            ans1 = i
            found1 = True
        if len(currSet2) == 14 and not found2:
            ans2 = i
            found2 = True        
        if i >= 4:
            curr[line[i-4]] -= 1
            if curr[line[i-4]] == 0:
                currSet.discard(line[i-4])
        if i >= 14:
            curr2[line[i-14]] -= 1
            if curr2[line[i-14]] == 0:
                currSet2.discard(line[i-14])
        curr2[line[i]] += 1
        currSet2.add(line[i])
        curr[line[i]] += 1
        currSet.add(line[i])
print(ans1)
print(ans2)
