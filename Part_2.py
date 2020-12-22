from itertools import combinations


open = open("input.txt", "r")
content = open.read()

splitlist = content.split("\n")
del splitlist[200]

final = list(map(int, splitlist))

combs = combinations(final, 3)

for c in combs:
    if sum(c) == 2020:
        print(c)
