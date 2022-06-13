def extract ():
    name = line.strip().split()
    return name


with open ("names.txt","r") as fin:
    fin.readline()
    dictName = {}
    for line in fin:
        nameList = extract ()
        fn = nameList[0]
        ln = nameList[-1]
        
        if ln in dictName:
            dictName[ln].append(fn)
        else:
            dictName[ln] = []
            dictName[ln].append(fn)

for i in dictName:
    print(i, ":" ,dictName[i])

