def countdown(n):
    if n == 0:
        print("BOOM!!!")
    else:
        print (n, " ")
        countdown (n-1)
    return

n = int(input("n?"))
countdown(n)