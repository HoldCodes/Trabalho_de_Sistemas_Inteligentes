from asyncio.windows_events import NULL
import sys
import os
import time
from tracemalloc import stop
from turtle import position

## Importa as classes que serao usadas
sys.path.append(os.path.join("pkg"))
from pkg.model import Model
from pkg.agentRnd import AgentRnd


class Stack:
    """
    Essa classe implementa a estrutura de dados chamada "pilha"
    """

    def __init__(self):
        self.__stack = []

    def push(self, value):
        """ Adiciona o valor (value) ao final da pilha """
        self.__stack.append(value)

    def pop(self):
        """ Remove o último valor da pilha """
        return self.__stack.pop()
    
    def isEmpty(self):
        return True if len(self.__stack) == 0 else False

    def show(self):
        """ Imprime a pilha no console """
        print(f'Stack: {self.__stack}')




## Metodo utilizado para permitir que o usuario construa o labirindo clicando em cima
def buildMaze(model):
    model.drawToBuild()
    step = model.getStep()
    while step == "build":
        model.drawToBuild()
        step = model.getStep()
    ## Atualiza o labirinto
    model.updateMaze()


def main():
    # Lê arquivo config.txt

    arq = open(os.path.join("config_data", "config.txt"), "r")
    configDict = {}
    for line in arq:
        ## O formato de cada linha é:var=valor
        ## As variáveis são 
        ##  maxLin, maxCol que definem o tamanho do labirinto
        ## Tv e Ts: tempo limite para vasculhar e tempo para salvar
        ## Bv e Bs: bateria inicial disponível ao agente vasculhador e ao socorrista
        ## Ks :capacidade de carregar suprimentos em número de pacotes (somente para o ag. socorrista)

        values = line.split("=")
        configDict[values[0]] = int(values[1])

    print("dicionario config: ", configDict)

    # Cria o ambiente (modelo) = Labirinto com suas paredes
    mesh = "square"

    ## nome do arquivo de configuracao do ambiente - deve estar na pasta <proj>/config_data
    loadMaze = "ambiente"

    model = Model(configDict["maxLin"], configDict["maxCol"], mesh, loadMaze)
    buildMaze(model)

    model.maze.board.posAgent
    model.maze.board.posGoal
    # Define a posição inicial do agente no ambiente - corresponde ao estado inicial
    model.setAgentPos(model.maze.board.posAgent[0], model.maze.board.posAgent[1])
    model.setGoalPos(model.maze.board.posGoal[0], model.maze.board.posGoal[1])
    model.draw()

    # Cria um agente
    agent = AgentRnd(model, configDict)

    pilha = Stack()

    ## Ciclo de raciocínio do agente
    i = 0
    while i != 1000:
        i += 1
    
        agent.deliberate(pilha, agent)
        model.draw()
        time.sleep(0.5)  # para dar tempo de visualizar as movimentacoes do agente no labirinto
    model.draw()


if __name__ == '__main__':
    main()
