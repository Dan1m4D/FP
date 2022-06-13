from tkinter import filedialog

def main():
    # 1) Pedir nome do ficheiro (experimente cada alternativa):
    #name = input("File? ")                                  #A
    name = filedialog.askopenfilename(title="Choose File") #B
    
    # 2) Calcular soma dos números no ficheiro:
    total = fileSum(name)
    
    # 3) Mostrar a soma:
    print("Sum:", total)


def fileSum(filename):
    with open (filename , "r") as fin:
        sum = 0
        filename.strip("/n")
        for line in fin:
            print(line)
            lineflt = float(line)
            sum += lineflt
    return sum

if __name__ == "__main__":
    main()

