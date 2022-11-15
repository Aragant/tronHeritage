from envi import ACTION_MOVE, SCREEN_HEIGHT, SCREEN_WIDTH, SPRITE_SCALE, SPRITE_OFFSET, RADAR_SIZE, ACTIONS, FILE_AGENT, ALPHA, GAMMA
import os
import pickle

class Agent:
    def __init__(self, env, filePath = 'agent.al1', alpha = ALPHA, gamma = GAMMA, cooling_rate = 0.999):
        self.__env = env
        self.__alpha = alpha
        self.__gamma = gamma
        self.__cooling_rate = cooling_rate
        self.__file = filePath

        self.__qTable = {}


        states = self.init_states()


        for state in states:
            self.__qTable[state] = {}
            for action in ACTIONS:
                self.__qTable[state][action] = 0.0

        self.__qTable["step"] = 0

        

        self.reset()

    def best_action(self):
        q = self.__qTable[self.__state]
        self.__currentAction = max(q, key=q.get)
        return  self.__currentAction

    
    def reset(self):
        self.__state = "000000000"
        self.__score = 0
        

    def init_states(self):
        states = []
        radarSize = 9

        for i in range(0, 2**radarSize):
            states.append(bin(i)[2:].zfill(radarSize))
            
        
        return states
    
    def load(self, filename):
        with open(filename, 'rb') as file:
            self.__qTable = pickle.load(file)

    def save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump((self.__qTable), file)


    def step(self, state, reward):
        
        maxQ = max(self.__qTable[state].values())
        
        delta = self.__alpha * (reward + self.__gamma * maxQ - self.__qTable[self.__state][self.__currentAction])

        self.__score += reward
        self.__qTable[self.__state][self.__currentAction] += delta
        self.__state = state
        
        self.__qTable["step"] += 1

    @property
    def getStep(self):
        return self.__qTable["step"]