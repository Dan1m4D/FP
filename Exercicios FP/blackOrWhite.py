inputStr = input("Casa no Tabuleiro?")

col = ['a','b','c','d','e','f','g','h']
row = [1,2,3,4,5,6,7,8]

c = inputStr[0]
r = int(inputStr[1])


if not (c in col or r in row):
   assert "Not in board"
else:
   if r % 2 != 0:
      if c in col[::2]:
         print("Black")
      else:
         print("White")
   else:
      if c in col[::2]:
         print("White")
      else:
         print("Black")
         