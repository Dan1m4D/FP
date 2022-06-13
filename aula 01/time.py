s=int(input("Insira o tempo em segundos: "))
sout= s%60 # --> segundos que imprimo
m= s//60 # --> minutos para calculo, ou seja, o nº de minutos total
mout= m%60 # --> minutos que quero imprimir, ou seja, o resto da operação das horas
h= m//60 # --> horas
print("Hora: {:02d}:{:02d}:{:02d}". format(h, mout, sout))

#1   - 00:00:01
#61  - 00:01:01
#3661- 01:01:01