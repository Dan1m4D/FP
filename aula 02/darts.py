#Importação de funções
import math

#Input de coordenadas cartesianas

x = float(input("Coordenada no x em milímetros?"))
y = float(input("Coordenada no y em milímetros?"))

#Transformação em coordenadas polares

r = math.sqrt(math.pow(x,2)+math.pow(y,2))

if y == 0:
    if x >= 0:
        a = 0
    elif x < 0:
        a = math.pi
else:
    a = math.atan2(y,x)

a = math.degrees(a)

#Condições de raio

m = 1 # "m" é o multiplicativo

if r <= 6.35:
    score = 50
    print("A sua pontuação é: ", score)
    exit()
elif r <= 16:
    score = 25
    print("A sua pontuação é: ", score)
    exit()
elif r <= 99:
    m = 2
elif r <= 107:
    m = 3
elif r<= 162:
    m = 1
elif r <= 170:
    m = 3
else:
    score = 0
    print("OUT")
    print("A sua pontuaçã é: 0")
    exit()

#Definição do setor

s = 0

if a <= 9 or (a >= 351 and a<= 360):
    s = 6
elif a <= 27:
    s = 13
elif a <= 45:
    s = 4
elif a <= 63:
    s = 18
elif a <= 81:
    s = 1
elif a <= 99:
    s = 20
elif a <= 117:
    s = 5
elif a <= 135:
    s = 12
elif a <= 153:
    s = 9
elif a <= 171:
    s = 14
elif a <= 189:
    s = 11
elif a <= 207:
    s = 8
elif a <= 225:
    s = 16
elif a <= 243:
    s = 7
elif a <= 261:
    s = 19
elif a <= 279:
    s = 3
elif a <= 297:
    s = 17
elif a <= 315:
    s = 2
elif a <= 333:
    s = 15
elif a <= 351:
    s = 10

#Cálculo do resultado

score = s*m

print("A sua pontuação é: ", score)