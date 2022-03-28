import numpy as np
from pkg.mapa import mapa
from pkg.robo import Robo

# Pular uma linha no depois da ultima vitima
# Se for mudar o ambiente mudar o limite do mapa no config.txt 


def formata(linha):
    formLine = []
    salva = ""
    for c in linha:
        if c == "," or c == "\n" or c == " ":
            if c != "" and salva.isdigit():
                formLine.append(salva)
                salva = ""

        if c.isdigit():
            salva = salva + c

    return formLine


def cria_mapa(lim_x, lim_y):

    #arq = open("data/ambiente.txt", "r")
    arq = open("data/ambiente2.txt", "r")
    lines = arq.readlines()

    agent = formata(lines[0])
    goal = formata(lines[1])
    paredes = formata(lines[2])
    vitimas = formata(lines[3])

    print(vitimas)

    tabuleiro = np.zeros((int(lim_x), int(lim_y)), dtype=str)

    tabuleiro[int(agent[0])][int(agent[1])] = 'A'
    tabuleiro[int(goal[0])][int(goal[1])] = 'G'

    x = -2

    for i in range(0, int(len(paredes)/2)):
        x = x + 2
        tabuleiro[int(paredes[x])][int(paredes[x+1])] = 'P'

    x = -2
    for i in range(0, int(len(vitimas)/2)):
        x = x + 2
        tabuleiro[int(vitimas[x])][int(vitimas[x+1])] = 'V'

    return tabuleiro


def main():

    # Lê arquivo config.txt
    configDict = {}
    arq = open("data/config.txt", "r")
    for line in arq:
        values = line.split("=")
        configDict[values[0]] = int(values[1])
    print("dicionario config: ", configDict)

    ## Cria o mapa
    tabuleiro = cria_mapa(configDict["maxLin"], configDict["maxCol"])
    ## Cria o robo
    cria_robo = Robo(tabuleiro)

    ## Tudo é passado para o mapa, lá é o mainloop
    instancia = mapa(configDict["maxLin"], configDict["maxCol"], tabuleiro, cria_robo)
    instancia.run()


if __name__ == '__main__':
    main()
