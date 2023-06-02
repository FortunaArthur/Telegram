import random

class JogoVelha:
    def __init__(self):
        self.limparTabuleiro()

    def exibirTabuleiro(self):
        print("\n")
        print(" " + self.tabuleiro[0][0] + " | " + self.tabuleiro[0][1] + " | " + self.tabuleiro[0][2])
        print("------------")

        print(" " + self.tabuleiro[1][0] + " | " + self.tabuleiro[1][1] + " | " + self.tabuleiro[1][2])
        print("------------")

        print(" " + self.tabuleiro[2][0] + " | " + self.tabuleiro[2][1] + " | " + self.tabuleiro[2][2])
        print("\n")

    def limparTabuleiro(self):
        self.tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.termino = ""

    def verificarVitoria(self):
        dicionarioVitoria = {}

        for i in ["X", "O"]:
            # Verificação Horizontal
            dicionarioVitoria[i] = (self.tabuleiro[0][0] == self.tabuleiro[0][1] == self.tabuleiro[0][2] == i)
            dicionarioVitoria[i] = (self.tabuleiro[1][0] == self.tabuleiro[1][1] == self.tabuleiro[1][2] == i) or dicionarioVitoria[i]
            dicionarioVitoria[i] = (self.tabuleiro[2][0] == self.tabuleiro[2][1] == self.tabuleiro[2][2] == i) or dicionarioVitoria[i]

            # Verificação Vertical
            dicionarioVitoria[i] = (self.tabuleiro[0][0] == self.tabuleiro[1][0] == self.tabuleiro[2][0] == i) or dicionarioVitoria[i]
            dicionarioVitoria[i] = (self.tabuleiro[0][1] == self.tabuleiro[1][1] == self.tabuleiro[2][1] == i) or dicionarioVitoria[i]
            dicionarioVitoria[i] = (self.tabuleiro[0][2] == self.tabuleiro[1][2] == self.tabuleiro[2][2] == i) or dicionarioVitoria[i]

            # Verificação Diagonal
            dicionarioVitoria[i] = (self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] == i) or dicionarioVitoria[i]
            dicionarioVitoria[i] = (self.tabuleiro[2][0] == self.tabuleiro[1][1] == self.tabuleiro[0][2] == i) or dicionarioVitoria[i]

        if dicionarioVitoria["X"]:
            self.termino = "x"
            print("X Ganhou")
            print("\n"*3)
            return

        elif dicionarioVitoria["O"]:
            self.termino = "o"
            print("O Ganhou")
            print("\n"*3)
            return

        empate = True
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == " ":
                    empate = False
                    break
            if not empate:
                break

        if empate:
            self.termino = "d"
            print("Empatou")
            print("\n"*3)

            return
            
    def jogadasUsuario(self):
        jogadaInvalida = True

        while jogadaInvalida:
            try:
                x = int(input("Digite a Linha da proxima Jogada (0 - 2): "))
                y = int(input("Digite a Coluna da proxima Jogada (0 - 2): "))

                if x > 2 or x < 0 or y > 2 or y < 0:
                    print("Jogada Inavlida")

                if self.tabuleiro[x][y] != " ":
                    print("Posição ja Preenchida")
                    continue

            except Exception as erro:
                print(erro)
                continue

            jogadaInvalida = False
        self.tabuleiro[x][y] = "X"

    def jogadasPC(self):
        jogadasPossiveis = []

        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == " ":
                    jogadasPossiveis.append((i, j))

        if len(jogadasPossiveis) > 0:
            x, y = random.choice(jogadasPossiveis)
            self.tabuleiro[x][y] = "O"
    
jogo = JogoVelha()
fim = 0

while fim == 0:
    jogo.exibirTabuleiro()

    while jogo.termino == "":
        jogo.jogadasUsuario()
        jogo.jogadasPC()

        jogo.exibirTabuleiro()
        jogo.verificarVitoria()
        
    print(
        "Você quer jogar de novo?\n" 
        "1 - SAIR |||||| 2 - JOGAR NOVAMENTE\n"
        "O QUE VOCÊ VAI ESCOLHER?: ")

    while True:
        fim = int(input())
        if fim == 1 or fim == 2:
            break
        else:
            print("OPÇÃO INVÁLIDA. DIGITE 1 OU 2.")

    if fim == 1:
        False
        break

    elif fim == 2:
        jogo.limparTabuleiro()
        fim = 0

    else:
        print("NÃO TEM ESSA OPÇÃO!")

# MANDEI O CHAT GPD LER E ENETNEDER ESSE CODIGO PQ JA TO PUTO SÃO 3:16 DA MANHA, E EU N SIE + QQ SE PASSA

# Entendi. O código fornecido parece ser uma implementação do jogo da velha em Python. É um jogo onde um jogador joga como "X" e o outro como "O". Aqui está uma descrição geral do funcionamento do código:

# A classe JogoVelha é definida com métodos para inicializar o tabuleiro, exibir o tabuleiro, limpar o tabuleiro, verificar vitória, jogadas do usuário e jogadas do computador.
# O método exibirTabuleiro imprime o tabuleiro atualizado na tela.
# O método limparTabuleiro redefine o tabuleiro para um estado inicial vazio.
# O método verificarVitoria verifica se há um vencedor ou um empate no jogo.
# O método jogadasUsuario permite que o jogador insira sua jogada.
# O método jogadasPC escolhe uma jogada aleatória para o computador.
# O código principal cria uma instância do objeto JogoVelha e começa um loop onde o tabuleiro é exibido, as jogadas do usuário e do computador são feitas, e a vitória é verificada. Após cada partida, é perguntado ao jogador se ele deseja jogar novamente.
# Se você tiver alguma pergunta específica ou precisar de ajuda com alguma parte do código, sinta-se à vontade para me perguntar.

