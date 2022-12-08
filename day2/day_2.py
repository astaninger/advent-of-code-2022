ans = 0
ans2 = 0
with open("input.txt") as f:
    for line in f:
        print(line.strip(), ans)
        opp, me = line.strip().split(" ")
        if (opp == "A" and me == "Y") or (opp == "B" and me == "Z") or (opp=="C" and me =="X"):
            ans += 6
        elif (opp == "A" and me == "X") or (opp == "B" and me == "Y") or (opp == "C" and me == "Z"):
            ans += 3

        if me == "X":
            ans += 1
        elif me == "Y":
            ans += 2
        else:
            ans +=3

        if opp == "A":
            if me == "X":
                ans2 += 3
            elif me == "Y":
                ans2 += 4
            else:
                ans2 += 8
        elif opp == "B":
            if me == "X":
                ans2 += 1
            elif me == "Y":
                ans2 += 5
            elif me == "Z":
                ans2 += 9
        else:
            if me == "X":
                ans2 += 2
            elif me == "Y":
                ans2 += 6
            else:
                ans2 += 7

        print(line.strip(), opp, me, ans)
print(ans)
print(ans2)

