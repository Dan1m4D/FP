
def list_creation():
    msg = """----Build a list----"""
    print(msg)
    lst = []
    while True:
        n = input("WRITE A NUMBER: ")
        if n == "":
            break
        a = int(n)
        lst.append(a)
    return lst 

def med_of_n(lst,n):
    sum = 0
    if n <= 0:
        print ("YOU CAN'T DIVIDE FOR 0")
        return "Exiting..."
    else:
        nlst = lst[:n]    
        for x in nlst:
            sum += x
        md = sum/n
        return md

# main function

lst = list_creation()
n = int(input("NUMBER? "))
med = med_of_n(lst, n)

print(med)