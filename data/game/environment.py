from envi import ACTION_MOVE

class Environment:
    def __init__(self):
        self.__start = "000000000"

        def do(self, state, action):
            move =  ACTION_MOVE[action]
            return move


    # def do():


    @property
    def start(self):
        return self.__start
