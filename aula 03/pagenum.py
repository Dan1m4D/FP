def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

def main() :
   page = int(input("Enter page number: "))
   if isEven(page) == True :
      print(page)
   else :
      print("%60d" % page)

  
main()