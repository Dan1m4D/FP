def fr(n):
    if n<10:
        n=fr(n+1)
    return n

n = int(input("n?"))

int(input(fr(n)))

print(fr(n))        