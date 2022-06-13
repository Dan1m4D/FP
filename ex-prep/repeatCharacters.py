def repeatCharacters(s,n):
    repeat = ""
    for i in s:
        repeat += i*n
    return str(repeat)

s = input("Escreva a palavra: ")
n = int(input("Número de vezes: "))

print(repeatCharacters(s,n))