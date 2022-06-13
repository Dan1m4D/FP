def factorial(n):
   assert isinstance(n, int)
   assert n >= 0            
   if n == 0:
       return 1
   return n*factorial(n-1)

print(factorial(int(input("n?"))))

# para calculos repetitivos como n*n-1*n-2*... posso invocar a função repetidamente