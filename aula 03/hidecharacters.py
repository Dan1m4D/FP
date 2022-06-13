def hideCharacters(str) :
   dig = 0
   for char in str:
      dig = dig + 1
   return "*"*dig

def main():
   word = input("Escreve uma palavra: ")
   secret = hideCharacters (word)
   print (secret)

main()