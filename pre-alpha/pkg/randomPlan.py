from asyncio.windows_events import NULL
from random import randint
#from pkg.agentRnd import AgentRnd
from state import State
#eu
from cardinal import *

class Stack:
    """
    Essa classe implementa a estrutura de dados chamada "pilha"
    """

    def __init__(self):
        self.__stack = []

    def isEmpty(self):
        return True if len(self.__stack) == 0 else False

    def push(self, value):
        """ Adiciona o valor (value) ao final da pilha """
        self.__stack.append(value)

    def pop(self):
        """ Remove o último valor da pilha """
        return self.__stack.pop()

    def show(self):
        """ Imprime a pilha no console """
        print(f'Stack: {self.__stack}')



class RandomPlan:
    def __init__(self, maxRows, maxColumns, goal, initialState, name = "none", mesh = "square"):
        """
        Define as variaveis necessárias para a utilização do random plan por um unico agente.
        """
        self.walls = []
        self.maxRows = maxRows
        self.maxColumns = maxColumns
        self.initialState = initialState
        self.currentState = initialState
        self.goalPos = goal
        self.actions = []

    
    def setWalls(self, walls):
        row = 0
        col = 0
        for i in walls:
            col = 0
            for j in i:
                if j == 1:
                    self.walls.append((row, col))
                col += 1
            row += 1
       
        
    def updateCurrentState(self, state):
         self.currentState = state

    def isPossibleToMove(self, toState):
        """Verifica se eh possivel ir da posicao atual para o estado (lin, col) considerando 
        a posicao das paredes do labirinto e movimentos na diagonal
        @param toState: instancia da classe State - um par (lin, col) - que aqui indica a posicao futura 
        @return: True quando é possivel ir do estado atual para o estado futuro """


        ## vai para fora do labirinto
        if (toState.col < 0 or toState.row < 0):
            return False

        if (toState.col >= self.maxColumns or toState.row >= self.maxRows):
            return False
        
        if len(self.walls) == 0:
            return True
        
        ## vai para cima de uma parede
        if (toState.row, toState.col) in self.walls:
            return False

        # vai na diagonal? Caso sim, nao pode ter paredes acima & dir. ou acima & esq. ou abaixo & dir. ou abaixo & esq.
        delta_row = toState.row - self.currentState.row
        delta_col = toState.col - self.currentState.col

        ## o movimento eh na diagonal
        if (delta_row !=0 and delta_col != 0):
            if (self.currentState.row + delta_row, self.currentState.col) in self.walls and (self.currentState.row, self.currentState.col + delta_col) in self.walls:
                return False
        
        return True

    def OnlineDFSAgent(self, estadoAtual, AgentRnd, pilha):
        localVitima = AgentRnd.victimPresenceSensor
        #if localVitima == estadoAtual: AttributeError: 'function' object has no attribute 'row'
        #    return False
        if str(estadoAtual) not in AgentRnd.untried:
            AgentRnd.untried[str(estadoAtual)] = Stack() 
            AgentRnd.untried[str(estadoAtual)].push("NE")
            AgentRnd.untried[str(estadoAtual)].push("SO")
            AgentRnd.untried[str(estadoAtual)].push("NO")
            AgentRnd.untried[str(estadoAtual)].push("SE")
            AgentRnd.untried[str(estadoAtual)].push("O")
            AgentRnd.untried[str(estadoAtual)].push("N")
            AgentRnd.untried[str(estadoAtual)].push("L")
            AgentRnd.untried[str(estadoAtual)].push("S")

        if AgentRnd.previousState is not NULL: 
            AgentRnd.resultsCol[str(AgentRnd.previousAction)] = estadoAtual 
            AgentRnd.results[str(AgentRnd.previousState)] = AgentRnd.resultsCol[AgentRnd.previousAction]
         
            AgentRnd.unbacktracked[str(AgentRnd.previousState)] = Stack()
            AgentRnd.unbacktracked[str(AgentRnd.previousState)].push(AgentRnd.previousAction)

        if AgentRnd.untried[str(estadoAtual)].isEmpty():
            if AgentRnd.unbacktracked[str(estadoAtual)].isEmpty():
                return False
            else: #n tenho certeza se aqui ta certo
                print("Unbacktracked:")
                AgentRnd.unbacktracked[str(estadoAtual)].show()
                acaoB = AgentRnd.unbacktracked[str(estadoAtual)].pop()
                AgentRnd.previousAction = acaoB
                AgentRnd.resultsCol[acaoB] = acaoB
                AgentRnd.results[str(estadoAtual)] = AgentRnd.resultsCol[acaoB]
        else:
            print("Acoes Restantes:")
            AgentRnd.untried[str(estadoAtual)].show() 
            AgentRnd.previousAction = AgentRnd.untried[str(estadoAtual)].pop()  
            AgentRnd.untried[str(estadoAtual)].show() 
        AgentRnd.previousState = estadoAtual
        return AgentRnd.previousAction
        
            

    def randomizeNextPosition(self, agent, pilha):
         """ Sorteia uma direcao e calcula a posicao futura do agente 
         @return: tupla contendo a acao (direcao) e o estado futuro resultante da movimentacao """
         
         possibilities = ["N", "S", "L", "O", "NE", "NO", "SE", "SO"]
         movePos = { "N" : (-1, 0),
                    "S" : (1, 0),
                    "L" : (0, 1),
                    "O" : (0, -1),
                    "NE" : (-1, 1),
                    "NO" : (-1, -1),
                    "SE" : (1, 1),
                    "SO" : (1, -1)}
        
         if agent.tl > 7:
            resultado = self.OnlineDFSAgent(self.currentState, agent, pilha)
         else:
            if pilha.isEmpty() is False:
                lastStep = pilha.pop()
                pilha.show()
                if lastStep == "N":
                    resultado = "S"
                elif lastStep == "S":
                    resultado = "N"
                elif lastStep == "O":
                    resultado = "L"
                elif lastStep == "L":
                    resultado = "O"
                elif lastStep =="NE":
                    resultado = "SO"
                elif lastStep =="NO":
                    resultado = "SE"
                elif lastStep =="SE":
                    resultado = "NO"
                elif lastStep =="SO":
                    resultado = "NE"
            elif agent.currentState == agent.prob.initialState:
                agent.tl = 15
                resultado = self.OnlineDFSAgent(self.currentState, agent, pilha)
         
         if resultado == False:
            return self.previousAction
         else:
            movDirection = resultado
         state = State(self.currentState.row + movePos[movDirection][0], self.currentState.col + movePos[movDirection][1])

         return movDirection, state


    def chooseAction(self, agent, pilha):
        """ Escolhe o proximo movimento de forma aleatoria. 
        Eh a acao que vai ser executada pelo agente. 
        @return: tupla contendo a acao (direcao) e uma instância da classe State que representa a posição esperada após a execução
        """

        ## Tenta encontrar um movimento possivel dentro do tabuleiro 
        result = self.randomizeNextPosition(agent, pilha)


        #while not self.isPossibleToMove(result[1]): por enquanto desativei acho q nao precisa
        #    result = self.randomizeNextPosition(agent)

        return result


    def do(self):
        """
        Método utilizado para o polimorfismo dos planos

        Retorna o movimento e o estado do plano (False = nao concluido, True = Concluido)
        """
        
        nextMove = self.move()
        return (nextMove[1], self.goalPos == State(nextMove[0][0], nextMove[0][1]))   
    
     


        
       
        
        
