ans1 = 0
ans2 = 0
stacks = []
for _ in range(9):
    stacks.append([])
with open("input.txt") as f:
    for i, line in enumerate(f):
        if i < 8:
            i = 0
            j = 0
            while i < len(line)-1:
                i+= 1
                if line[i] != " ":
                    stacks[j].append(line[i])
                i+=3
                j+=1
                j%=9
            print(stacks)
        elif line[0] == " ":
            for i in range(len(stacks)):
                stacks[i] = list(reversed(stacks[i]))
        elif line[0] == "m":
            line = line.strip()
            _, num, _, src, _, dest = line.split(" ")
            print(line, num, src, dest)
            num = int(num)
            src = int(src)
            dest = int(dest)
            while num:
                stacks[dest-1].append(stacks[src-1].pop())
                num -= 1
            print(stacks)
    ans1 = "".join([stacks[i][-1] for i in range(len(stacks))])
    print(stacks)
stacks = []
for _ in range(9):
    stacks.append([])
with open("input.txt") as f:
    for i, line in enumerate(f):
        if i < 8:
            i = 0
            j = 0
            while i < len(line)-1:
                i+= 1
                if line[i] != " ":
                    stacks[j].append(line[i])
                i+=3
                j+=1
                j%=9
            print(stacks)
        elif line[0] == " ":
            for i in range(len(stacks)):
                stacks[i] = list(reversed(stacks[i]))
        elif line[0] == "m":
            line = line.strip()
            _, num, _, src, _, dest = line.split(" ")
            print(line, num, src, dest)
            num = int(num)
            src = int(src)
            dest = int(dest)
            stacks[dest-1] += stacks[src-1][-num:]
            while num:
                stacks[src-1].pop()
                num-=1
            print(stacks)
    ans2 = "".join([stacks[i][-1] for i in range(len(stacks))])
    print(stacks)
print(ans1)
print(ans2)
