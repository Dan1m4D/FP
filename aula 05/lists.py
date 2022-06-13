def fltlist():
    msg = """-----LISTS & U-----
    LET'S DO A LIST 2GETHER
    WRITE AS MANY NUMBERS AS YOU WANT
    WHEN YOU'RE DONE, PRESS ENTER TO
    COMPILE THE LIST"""
    print(msg)
    lst = []
    while True:
        n = input("WRITE A NUMBER: ")
        if n == "":
            break
        a = float(n)
        lst.append(a)
    return lst


def countlower(lst, v):
    c = 0
    for n in lst:
        if n < v:
            c = c + 1
    return c


def minmax(lst):
    #for n in lst:
    #   if
    return min(lst), max(lst)


def medlower(lst):
    mn, mx = minmax(lst)
    med = (mn+mx)/2
    medlow = countlower(lst, med)
    return med, medlow


l = fltlist()
print("LIST: ", l)
n = float(input("WRITE A NUMBER TO SEE SOMETHING AWESOME: "))
print("THERE ARE {} MINOR THAN {}".format(countlower(l, n), n))
print("THE MIN AND THE MAX ARE, RESPECTIVELY {}".format(minmax(l)))
med, medlow = medlower(l)
print("THE AVERAGE BETWEEN THE MAX AND THE MIN IS '{}' AND THERE ARE '{}' MINOR THAN THE AVERAGE".format(med, medlow))
