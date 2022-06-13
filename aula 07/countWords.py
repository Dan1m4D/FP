letterdic = {}

c = 0

with open ("pg3333.txt") as fin:
    for line in fin:
        l = line.strip
        for w in l:
            w