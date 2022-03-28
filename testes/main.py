import numpy as np
from pkg.mapa import mapa


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

    arq = open("data/ambiente.txt", "r")
    lines = arq.readlines()

    agent = formata(lines[0])
    goal = formata(lines[1])
    paredes = formata(lines[2])
    vitimas = formata(lines[3])

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
    #print("dicionario config: ", configDict)

    #leitura_arquivo(open("data/ambiente.txt", "r"), ambDict)
    #print("dicionario config: ", ambDict)
    ## Cria o mapa
    tabuleiro = cria_mapa(configDict["maxLin"], configDict["maxCol"])

    instancia = mapa(configDict["maxLin"], configDict["maxCol"], tabuleiro)
    instancia.run()

    #instancia.pintar_quadrado(8, 8, 'A')
    #tabuleiro[5][5] = 'A'
    #print(tabuleiro)


if __name__ == '__main__':
    main()
