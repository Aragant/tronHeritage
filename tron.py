import arcade
import os
import pickle


SPRITE_SCALE = 0.02
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SPRITE_OFFSET = 10
RADAR_SIZE = 10

ACTION_UP = 'U'
ACTION_DOWN = 'D'
ACTION_LEFT = 'L'
ACTION_RIGHT = 'R'
ACTIONS = [ACTION_UP, ACTION_DOWN, ACTION_LEFT, ACTION_RIGHT]
ACTION_MOVE = {
    ACTION_UP: (0, SPRITE_OFFSET),
    ACTION_DOWN: (0, -SPRITE_OFFSET),
    ACTION_LEFT: (-SPRITE_OFFSET, 0),
    ACTION_RIGHT: (SPRITE_OFFSET, 0)
}

FILE_AGENT = 'agent.al1'


class Environnement:
    def __init__(self):
        self.__start = "000000000"

        def do(self, state, action):
            move =  ACTION_MOVE[action]
            return move

    @property
    def start(self):
        return self.__start
class Agent:
    def __init__(self, env, filePath = 'agent.al1', alpha = 0.2, gamma = 1, cooling_rate = 0.999):
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

        print(self.__qTable)

        self.reset()

    def best_action(self):
        print("state : ", self.__state)
        q = self.__qTable[self.__state]
        print("q : ", q)
        return max(q, key = q.get)
    
    def step(self, ):
        self.__currentAction = self.best_action()
        print("action : ", self.__currentAction)
        return ACTION_MOVE[self.__currentAction]

    def updateReward(self, state, reward):
        
        maxQ = max(self.__qTable[state].values())
        
        delta = self.__alpha * (reward + self.__gamma * maxQ - self.__qTable[self.__state][self.__currentAction])
        print("score : ", self.__qTable[self.__state][self.__currentAction], " + ", delta)
        self.__qTable[self.__state][self.__currentAction] += delta
        self.__state = state
    
    def reset(self):
        self.__state = env.start
        
    def updateState(self, state):
        self.__state = state

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

    

class TronWindow(arcade.View):
    def __init__(self, agentJ1, agentJ2):
        super().__init__()
        self.__agentJ1 = agentJ1
        self.__agentJ2 = agentJ2

        self.__obstacles = arcade.SpriteList()
        self.__j1 = arcade.Sprite('boxBlue.png', image_height=10, image_width=10)
        self.__j2 = arcade.Sprite('boxRed.png', image_height=10, image_width=10)

        self.__j1.center_x, self.__j1.center_y = SCREEN_WIDTH / 2 + 20, SCREEN_HEIGHT / 2
        self.__j2.center_x, self.__j2.center_y = SCREEN_WIDTH / 2 - 20, SCREEN_HEIGHT / 2

        self.__j1direction_x, self.__j1direction_y = SPRITE_OFFSET, 0
        self.__j2direction_x, self.__j2direction_y = - SPRITE_OFFSET, 0

        self.__j1Radar = self.init_radar(self.__j1)
        self.__j2Radar = self.init_radar(self.__j2)

        self.__j1state = self.getRadarState(self.__j1Radar)
        self.__j2state = self.getRadarState(self.__j2Radar)

        print(self.__j1.height, self.__j1.width)

        self.__obstacles.append(self.__j1)
        self.__obstacles.append(self.__j2)

        self.__win = 0

    
    def init_radar(self, player):
        radar = []

        boxPath = "boxViolet.jpg"

        case1 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case1.center_x, case1.center_y = player.center_x, player.center_y
        case2 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case2.center_x, case2.center_y = player.center_x - SPRITE_OFFSET, player.center_y
        case3 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case3.center_x, case3.center_y = player.center_x + SPRITE_OFFSET, player.center_y 
       
        case4 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case4.center_x, case4.center_y = player.center_x, player.center_y + SPRITE_OFFSET
        case5 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case5.center_x, case5.center_y = player.center_x - SPRITE_OFFSET, player.center_y + SPRITE_OFFSET
        case6 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case6.center_x, case6.center_y = player.center_x + SPRITE_OFFSET, player.center_y + SPRITE_OFFSET

        case7 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case7.center_x, case7.center_y = player.center_x, player.center_y - SPRITE_OFFSET
        case8 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case8.center_x, case8.center_y = player.center_x - SPRITE_OFFSET, player.center_y - SPRITE_OFFSET
        case9 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case9.center_x, case9.center_y = player.center_x + SPRITE_OFFSET, player.center_y - SPRITE_OFFSET

        radar.append(case1)
        radar.append(case2)
        radar.append(case3)
        radar.append(case4)
        radar.append(case5)
        radar.append(case6)
        radar.append(case7)
        radar.append(case8)
        radar.append(case9)

        return radar



    def on_draw(self):
        
        arcade.start_render()
        self.__j1.draw()
        self.__j2.draw()
        self.__obstacles.draw()
        for case in self.__j1Radar:
            case.draw()
        for case in self.__j2Radar:
            case.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            if self.__j1direction_y != - SPRITE_OFFSET:
                self.__j1direction_x, self.__j1direction_y = 0, SPRITE_OFFSET
        elif key == arcade.key.DOWN:
            if self.__j1direction_y != SPRITE_OFFSET:
                self.__j1direction_x, self.__j1direction_y = 0, - SPRITE_OFFSET
        elif key == arcade.key.LEFT:
            if self.__j1direction_x != SPRITE_OFFSET:
                self.__j1direction_x, self.__j1direction_y = - SPRITE_OFFSET, 0
        elif key == arcade.key.RIGHT:
            if self.__j1direction_x != - SPRITE_OFFSET:
                self.__j1direction_x, self.__j1direction_y = SPRITE_OFFSET, 0

        if key == arcade.key.W:
            if self.__j2direction_y != - SPRITE_OFFSET:
                self.__j2direction_x, self.__j2direction_y = 0, SPRITE_OFFSET
        elif key == arcade.key.S:
            if self.__j2direction_y != SPRITE_OFFSET:
                self.__j2direction_x, self.__j2direction_y = 0, - SPRITE_OFFSET
        elif key == arcade.key.A:
            if self.__j2direction_x != SPRITE_OFFSET:
                self.__j2direction_x, self.__j2direction_y = - SPRITE_OFFSET, 0
        elif key == arcade.key.D:
            if self.__j2direction_x != - SPRITE_OFFSET:
                self.__j2direction_x, self.__j2direction_y = SPRITE_OFFSET, 0
    
    def on_update(self, delta_time: float):
        # self.__obstacles.append(self.__j1)
        # self.__obstacles.append(self.__j2)

        direction = self.__agentJ1.step()
        self.__j1direction_x, self.__j1direction_y = direction[0], direction[1]

        direction = self.__agentJ2.step()
        self.__j2direction_x, self.__j2direction_y = direction[0], direction[1]

        j1Next = arcade.Sprite('boxBlue.png', image_height=10, image_width=10)
        j1Next.center_x, j1Next.center_y = self.__j1.center_x + self.__j1direction_x, self.__j1.center_y + self.__j1direction_y
        self.__j1 = j1Next

        j2Next = arcade.Sprite('boxRed.png', image_height=10, image_width=10)
        j2Next.center_x, j2Next.center_y = self.__j2.center_x + self.__j2direction_x, self.__j2.center_y + self.__j2direction_y 
        self.__j2 = j2Next

        self.__j1Radar = self.init_radar(self.__j1)
        self.__j2Radar = self.init_radar(self.__j2)



        j1state = self.getRadarState(self.__j1Radar)
        j2state = self.getRadarState(self.__j2Radar)

        
        



        if arcade.check_for_collision_with_list(self.__j1, self.__obstacles) or not self.isInside(self.__j1.center_x, self.__j1.center_y):
            self.__agentJ1.updateReward(j1state, -1000)
            # self.__agentJ2.updateReward(j2state, 100)
            self.reset()
            # self.window.show_view(WinView("Red"))
        else:
            self.__agentJ1.updateReward(j1state, 0)


        if arcade.check_for_collision_with_list(self.__j2, self.__obstacles) or not self.isInside(self.__j2.center_x, self.__j2.center_y):
            # self.__agentJ1.updateReward(j1state, 100)
            self.__agentJ2.updateReward(j2state, -1000)
            self.reset()
            # self.window.show_view(WinView("Blue"))
        else:
            self.__agentJ2.updateReward(j2state, 0)

        if arcade.check_for_collision(self.__j1, self.__j2):
            self.__agentJ1.updateReward(j1state, -1000)
            self.__agentJ2.updateReward(j2state, -1000)
            self.reset()
            # self.window.show_view(WinView("Draw"))

        self.__obstacles.append(self.__j1)
        self.__obstacles.append(self.__j2)

    def reset(self):
        self.__agentJ1.reset()
        self.__agentJ2.reset()

        self.__j1.center_x, self.__j1.center_y = SCREEN_WIDTH / 2 + 20, SCREEN_HEIGHT / 2
        self.__j2.center_x, self.__j2.center_y = SCREEN_WIDTH / 2 - 20, SCREEN_HEIGHT / 2

        self.__obstacles = arcade.SpriteList()
        


    def getRadarState(self, radar):
        
        state = ""
        for case in radar:
            if arcade.check_for_collision_with_list(case, self.__obstacles) or not self.isInside(case.center_x, case.center_y):
                state += "1"
            else:
                state += "0"
        return state

    def isInside(self, x, y):
        return x >= 0 and x < SCREEN_WIDTH and y >= 0 and y < SCREEN_HEIGHT    


class WinView(arcade.View):
    def __init__(self, winner):
        super().__init__()
        self.__winner = winner

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(self.__winner + " win !!!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.WHITE, 32, anchor_x='center', anchor_y='center')
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.close_window()
        
        if key == arcade.key.SPACE:
            window = TronWindow()
            self.window.show_view(window)


if __name__ == '__main__':
    env = Environnement()
    qTableJ1FilePath = "qTableJ1"
    qTableJ2FilePath = "qTableJ2"
    agentJ1 = Agent(env, qTableJ1FilePath)
    agentJ2 = Agent(env, qTableJ2FilePath)
    
    if os.path.exists(qTableJ1FilePath):
        agentJ1.load(qTableJ1FilePath)

    if os.path.exists(qTableJ2FilePath):
        agentJ2.load(qTableJ2FilePath)

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "TRON HERITAGE")
    tronView = TronWindow(agentJ1, agentJ2)
    window.show_view(tronView)
    arcade.run()

    agentJ1.save(qTableJ1FilePath)
    agentJ2.save(qTableJ2FilePath)