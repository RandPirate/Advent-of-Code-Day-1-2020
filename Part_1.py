
open = open("input.txt", "r")
content = open.read()


splitlist = content.split("\n")
del splitlist[200]


final = list(map(int, splitlist))
print(final)
for i in final:
    calc = 2020 - i 
    if calc in final:
        print(calc)
    
# i + x = 2020
# x= 2020 - i