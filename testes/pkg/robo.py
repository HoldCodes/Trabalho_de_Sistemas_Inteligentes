import random


class Robo:
    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro

        self.robo_posi_x = 0
        self.robo_posi_y = 0

    def imprime(self):
        print()

    def sorteia(self):
        self.tabuleiro[random.randint(0, 24)][random.randint(0, 24)] = 'A'

    def deliberate(self):

        direcoes = ['U', 'D', 'L', 'R']

        sorteio = direcoes[random.randint(0,3)]

        x = 0
        y = 0

        if sorteio == 'U':
            x = -1
            y = 0
        elif sorteio == 'D':
            x = 1
            y = 0
        elif sorteio == 'L':
            x = 0
            y = -1
        elif sorteio == 'R':
            x = 0
            y = 1

        if self.robo_posi_x + x >= 0 and self.robo_posi_y + y >= 0:
            if self.robo_posi_x + x <= 24 and self.robo_posi_y + y <= 24:
                if self.tabuleiro[self.robo_posi_x + x][self.robo_posi_y + y] == "":
                    self.tabuleiro[self.robo_posi_x][self.robo_posi_y] = ''
                    self.robo_posi_x += x
                    self.robo_posi_y += y
                    self.tabuleiro[self.robo_posi_x][self.robo_posi_y] = 'A'

