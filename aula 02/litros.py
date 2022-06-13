l=float(input("Litros abastecidos?"))
p= l*1.40

if l > 40.0:
    p = p*0.90
else:
    p = p

print("O preço é: ", p)