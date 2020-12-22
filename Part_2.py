from itertools import combinations
# import numpy as np

open = open("input.txt", "r")
content = open.read()

splitlist = content.split("\n")
del splitlist[200]

final = list(map(int, splitlist))



# for i in range(len(final)):
#     for c in combinations(final, i):
#         combination = c

combs = combinations(final, 3)

for c in combs:
    if sum(c) == 2020:
        print(c)


# sol = [c for c in combs if sum(c) == 2020]

# print(sol)

# np.prod(sol)