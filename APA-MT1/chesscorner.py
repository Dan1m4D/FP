x = input("Cordenadas:")
def local(x):
    list = []
    for i in x:
        list.append(i)
    lcorner = ["a","b"]
    numcorner = ["1","8"]
    num = ["1","2","3","4","5","6","7","8"]
    l = ["a","b","c","d","e","f","g","h"]
    if (list[0] in lcorner and list[1] in numcorner):
        return "Corner"
    elif (list[0] in lcorner and list[1] in num or list[1] in numcorner and list[0] in l):
        return "Border"
    else:
        return "Inside"

print (local(x))
