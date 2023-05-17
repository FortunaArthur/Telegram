def Limpar(n_linhas):
    print("\n"*n_linhas)

carrosPatio = [
    ("Skyline do Braian", 400),
    ("Megas XRL", 500),
    ("Batmovel", 200),
    ("Toreto V8", 400),
    ("Opalão do vô", 600), 
    ("Van do Scooby-Doo", 100),
    ("Marea de Tião", 900),
    ("Carro Bomba de terrorista com certificado de aprovação de Osama Bin Laden mais seguro que o Marea", 1)]

carrosAlugados = []

def mostrarCarrinho(carro_lista):
    for cod, possante in enumerate(carro_lista):
        print("Codigo: {} - {} || Custa {} R$ Por Dia". format(cod, possante[0], possante[1]))
    
while True:
    print(  "Bem Vindo ao Patio do Detran, qq se veio fazer aki?:\n"
            "1 - Ver os Possantes\n"
            "2 - Alugar \n"
            "3 - Devolver o Carro Alugado \n"
            "0 - Vai Embora Daki Seu INNNSEEEETOO")
    
    try:
        escolha = int(input("QQ SE ESCOLHE?: "))

        if escolha == 0:
            print("VC Foi Muito é Tarde")
            Limpar(2)
            False
            break

        elif escolha == 1:
            Limpar(3)
            print("Patio onde Transformer chora e mãe não vê")
            mostrarCarrinho(carrosPatio)
            Limpar(5)

        elif escolha == 2:
            Limpar(3)
            print("Patio onde Transformer chora e mãe não vê")
            mostrarCarrinho(carrosPatio)
            Limpar(5)

            try:
                codiCarrinho = int(input("Qual Carro Vc vai Querer Alugar? CODIGO->: "))
                dias = int(input("Quantos Dias Vc vai Alugar?: "))
                Limpar(3)
                print("TU Alugou o Carro: ( {} ) por {} Dias, O Total do Aluguel vai ficar {} R$ ".format(carrosPatio[codiCarrinho][0], dias, (carrosPatio[codiCarrinho][1] * dias)))
                
                alugar = int(input("Deseja Alugar este Carro? \n"
                                   "1 - SIM     2- NÃO \n"
                                   "Escolha: "))
                try:
                    if alugar == 1:
                        Limpar(1)
                        print("Parabéns seu BIZONHO, tu Alugou o Carro: ( {} ) por {} Dias".format(carrosPatio[codiCarrinho][0], dias))
                        carrosAlugados.append(carrosPatio.pop(codiCarrinho))
                        Limpar(3)

                    elif alugar == 2:
                        print("Escolha Direito Então seu INSETO")
                        Limpar(4)
                        continue

                    else:
                        print("Opção Invalida seu INNNNSSEEEETO")

                except ValueError:
                    Limpar(2)
                    print("Codigo Errado")
                    Limpar(2)

            except ValueError:
                Limpar(2)
                print("Codigo Errado")
                Limpar(2)

        elif escolha == 3:
            if len(carrosAlugados) == 0:
                Limpar(1)
                print("Não tem Carro nenhum pra devolver, a num ser q se tenha roubado")
                Limpar(3)
            
            else:
                Limpar(2)
                print("Lista dos Carros Alugados")
                mostrarCarrinho(carrosAlugados)
                Limpar(1)

                try:
                    codiAluga = int(input("Qual carro se vai devolver: "))
                    chek = []
                    for i, k in enumerate(carrosAlugados):
                        chek.append(i)
                    
                    very = codiAluga in chek

                    if  very == True:
                        Limpar(1)
                        print("Obrigado seu BIZONHO, por devolver o Carro: ( {} ) o pagamento se acerta ali com ZERO MEIA".format(carrosAlugados[codiAluga][0]))
                        carrosPatio.append(carrosAlugados.pop(codiAluga))
                        Limpar(2)

                    else:
                        Limpar(2)
                        print("Não tem esse carro")
                        Limpar(2)

                except ValueError:
                    Limpar(2)
                    print("Codigo Errado")
                    Limpar(2)


        else:
            Limpar(20)
            print("Opção Invalida seu INNNNSSEEEETO")
            Limpar(5)

    except ValueError:
        Limpar(30)
        print("Digito Opção Certa ")
        Limpar(3)

