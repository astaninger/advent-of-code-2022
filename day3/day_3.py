ans = 0
ans2 = 0
with open("input.txt") as f:
    groups = []
    for line in f:
        print(line.strip(), ans)
        line = list(line.strip())
        groups.append(set(line))
        first, second = set(line[:len(line)//2]), set(line[len(line)//2:])
        same = list(first & second)[0]
        if same.lower() == same:
            ans += ord(same) - ord('a')+1
        else:
            ans += ord(same) - ord("A") + 27
        print(first, second)
    print(groups)
    for i in range(0, len(groups), 3):
        a = list(groups[i] & groups[i+1] & groups[i+2])[0]
        print(a)
        if a.lower() == a:
            ans2 += ord(a) - ord('a')+1
        else:
            ans2 += ord(a) - ord("A") + 27
print(ans)
print(ans2)

