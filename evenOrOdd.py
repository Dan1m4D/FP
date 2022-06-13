even = []
odd = []

while True>0:    
    x = int(input('N?'))
    
    if x <= 0:
        break
  
    if (x%2==0):
        even.append(x)
    else:
        odd.append(x)

print ('Even --> ', even)
print ('Odd --> ', odd)

    