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
        self.__history = []
        self.__score = 0

        self.__qTable = {}


        states = self.init_states()


        for state in states:
            self.__qTable[state] = {}
            for action in ACTIONS:
                self.__qTable[state][action] = 0.0

        print(self.__qTable)

        self.reset()

    def best_action(self):
        # print("state : ", self.__state)
        q = self.__qTable[self.__state]
        # print("q : ", q)
        return max(q, key = q.get)
    
    def step(self):
        self.__currentAction = self.best_action()
        state, reward = self.__env.do(self.__state, self.__currentAction)
        # print("action : ", self.__currentAction)

        # maxQ = max(self.__qTable[state].values())
        
        # delta = self.__alpha * (reward + self.__gamma * maxQ - self.__qTable[self.__state][action])
        # # print("score : ", self.__qTable[self.__state][action], " + ", delta)
        # self.__qTable[self.__state][action] += delta
        # self.__state = state

        return state

    
    def reset(self, append_score = True):
        if append_score:
            self.__history.append(self.__score)
        self.__state = "0000000000000"
        self.__score = 0
        
        
    def updateState(self, state):
        self.__state = state

    def init_states(self):
        states = []
        radarSize = 13

        for i in range(0, 2**radarSize):
            states.append(bin(i)[2:].zfill(radarSize))
            
        
        return states
    
    def load(self, filename):
        with open(filename, 'rb') as file:
            self.__qTable, self.__history = pickle.load(file)

    def save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump((self.__qTable, self.__history), file)

    # def step(self):
    #     self.__currentAction = self.best_action()
    #     print("action : ", self.__currentAction)
    #     return ACTION_MOVE[self.__currentAction]

    def updateReward(self, state, reward):
        
        maxQ = max(self.__qTable[state].values())
        
        delta = self.__alpha * (reward + self.__gamma * maxQ - self.__qTable[self.__state][self.__currentAction])
        self.__score += reward
        self.__qTable[self.__state][self.__currentAction] += delta
        self.__state = state
    
    @property
    def history(self):
        return self.__history