def Pular():
    print("======================")
    print("\n")

def Somar(x, y):
    print("Resultado: ", (x+y))
    Pular()

def Subtrair(x, y):
    print("Resultado: ", (x-y))
    Pular()

def Multiplicar(x, y):
    print("Resultado: ", (x*y))
    Pular()

def Dividir(x, y):
    if y == 0:
        print("NÃO PODE Dividir por ZERO")
        Pular()
    else:
        print("Resultado: ", (x/y))

def Exponenciar(x, y):
    if x == 0 or y == 0:
        print("É 1 (UM) PORRA")
        Pular()
    else:
        print("Resultado: ", (x**y))
        Pular()

def Menu():
    Pular()
    print("--MENU-- \n"
          "1 - Somar \n"
          "2 - Subtrair \n"
          "3 - Multiplicar \n"
          "4 - Dividir \n"
          "5 - Exponenciação \n"
          "6 - Sair / Fechar o Programa")


while True:
    Menu()
    OP = int(input("Escolha: "))
    Pular()

    
    if OP == 6:
        print("CABOOUU, FIM DO PROGRAMA")
        False
        break

    else: 
        N1 = float(input("1° Numero: "))
        N2 = float(input("2° Numero: "))

        if OP == 1:
            Somar(N1, N2)

        elif OP == 2:
            Subtrair(N1, N2)

        elif OP == 3:
            Multiplicar(N1, N2)

        elif OP == 4:
            Dividir(N1, N2)
        
        elif OP == 5:
            Exponenciar(N1, N2)
        
        