def fib(x):
        if x == 0:
            return 0
        if x == 1:
            return 1
        f = fib(x-1) + fib(x-2)
        return f

n=int(input("n?"))
print(fib(n))
exit()

