import numpy as np
import tkinter
from tkinter import *


class mapa:
    def __init__(self, x, y, tabuleiro):

        self.limite_x = x
        self.limite_y = y

        self.paredes = []
        self.vitimas = []

        self.window = tkinter.Tk()
        self.window.geometry("800x800")
        # self.window.resizable(False, False)

        self.x = 0
        self.y = 0

        self.tabuleiro = tabuleiro

        #self.container2 = Frame(self.window)
        #self.container2.grid(column=1, row=0)
        #Button(self.container2, command=lambda: self.pintar_quadrado(self.x, self.y), text="BOTAO").grid(column=0, row=0)

        self.container1 = Canvas(self.window, width=800, height=800)

        x = 0
        y = 0

        for i in range(0, self.limite_x):
            y = i * 32
            for j in range(0, self.limite_y):
                x = j * 32
                self.container1.create_rectangle(x, y, x + 32, y + 32)

        self.container1.grid(column=0, row=0)

        ## altera a cor do quadrado
        # self.container1.itemconfig(625, fill="blue")
        #print(self.mapa)

    def desenha(self):

        for i in range(0, self.limite_x):
            for j in range(0, self.limite_y):
                if self.tabuleiro[i][j] == 'A':
                    self.pintar_quadrado(i, j, 'A')

                elif self.tabuleiro[i][j] == 'G':
                    self.pintar_quadrado(i, j, 'G')

                elif self.tabuleiro[i][j] == 'P':
                    self.pintar_quadrado(i, j, 'P')

                elif self.tabuleiro[i][j] == 'V':
                    self.pintar_quadrado(i, j, 'V')

                else:
                    self.pintar_quadrado(i, j, 'K')

    def pintar_quadrado(self, x, y, tipo):

        contador = (x * self.limite_y) + y + 1

        if tipo == 'A':
            self.container1.itemconfig(contador, fill="blue")
        elif tipo == 'G':
            self.container1.itemconfig(contador, fill="yellow")
        elif tipo == 'P':
            self.container1.itemconfig(contador, fill="black")
        elif tipo == 'V':
            self.container1.itemconfig(contador, fill="green")
        else:
            self.container1.itemconfig(contador, fill="white")

    def atualiza_agente_vasculhador(self):
        print()
        #self.container1.itemconfig(cont, fill="black")

    def run(self):
        while True:
            try:
                self.desenha()
            except:
                pass
            self.window.update_idletasks()
            self.window.update()
