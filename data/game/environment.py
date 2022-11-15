from envi import ACTION_MOVE
import arcade

class Environment:
    def __init__(self):
        self.__j1Start = (0, 20)
        self.__j2Start = (0, -20)

            

    def do(self, j1state, action):
        move =  ACTION_MOVE[action]
        
        
        return move, 0


