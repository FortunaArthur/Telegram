import random;

armas = ["Pedra", "Papel", "Tesoura"]

placarVC = 0
placarPC = 0


def Jogo():
    global placarPC, placarVC

    try:
        vc = int(input("1-Pedra  2-Papel  3-Tesoura\n"
                       "O que vc escolhe?: "))
        print()

        if vc == 1:
            vcop = armas[0]

            if pc == "Papel":
                print("VC escolheu: {} \n"
                    "O PC escolheu: {}".format(vcop, pc))
                
                print()

                print("VC Perdeu\n")
                placarPC = placarPC + 1

                
            elif pc == "Tesoura":
                print("VC escolheu: {} \n"
                    "O PC escolheu: {}".format(vcop, pc))

                print()

                print("VC Ganhou\n")
                placarVC = placarVC + 1

            else:
                print("VC escolheu: {} \n"
                    "O PC escolheu: {}".format(vcop, pc))
                print("Deu Empate\n")

        elif vc == 2:
            vcop = armas[1]
            
            if pc == "Tesoura":
                print("VC escolheu: {} \n"
                    "O PC escolheu: {}".format(vcop, pc))
                
                print()

                print("VC Perdeu\n")
                placarPC = placarPC + 1

                
            elif pc == "Pedra":
                print("VC escolheu: {} \n"
                    "O PC escolheu: {}".format(vcop, pc))

                print()

                print("VC Ganhou\n")
                placarVC = placarVC + 1

            else:
                print("VC escolheu: {} \n"
                    "O PC escolheu: {}".format(vcop, pc))
                print("Deu Empate\n")
            
        elif vc == 3:
            vcop = armas[2]
            
            if pc == "Pedra":
                print("VC escolheu: {} \n"
                    "O PC escolheu: {}".format(vcop, pc))
                
                print()

                print("VC Perdeu\n")
                placarPC = placarPC + 1

                
            elif pc == "Papel":
                print("VC escolheu: {} \n"
                    "O PC escolheu: {}".format(vcop, pc))

                print()

                print("VC Ganhou\n")
                placarVC = placarVC + 1

            else:
                print("VC escolheu: {} \n"
                    "O PC escolheu: {}".format(vcop, pc))
                print("Deu Empate\n")
    
        else:
            print("Escolheu ERRADO")

    except ValueError:
        print("Valor errado karai")

while True:
    try:
        
        pc = random.choice(armas)
        escolha = int(input("1 - Jogar   2 - Sair \n"
                            "QQ VC ESCOLHE?: "))
        print()
        
        if escolha == 2:
            print("Resulado")
            print("Placar:\n", "VC: {}  X  PC: {} \n".format(placarVC, placarPC))
            False
            break

        elif escolha == 1:
            print("Placar:\n", "VC: {}  X  PC: {} \n".format(placarVC, placarPC))
            Jogo()

        else:
            print("Opção Errado KARAI")

    except ValueError:
        print("ME MAMA")
