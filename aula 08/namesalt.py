from tkinter.font import names


with open('names.txt','r') as fin:
    fin.readline
    namesLst = []
    namesDic = {}
    for line in fin:
        Lst = line.strip().split()
        fname = Lst[0]
        lname = Lst[-1]
        
        for fname, mname, lname in fullName:
            if lname in namesDic.keys():
                namesDic[lname].append(fname)
            else:
                namesDic[lname] = fname

for i in namesDic:
    print (i ,':', namesDic[i] )