import arcade


SPRITE_SCALE = 0.01
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SPRITE_OFFSET = 6

REWARD_DEFAULT = -1

ACTION_UP = 'U'
ACTION_DOWN = 'D'
ACTION_LEFT = 'L'
ACTION_RIGHT = 'R'
ACTIONS = [ACTION_UP, ACTION_DOWN, ACTION_LEFT, ACTION_RIGHT]
ACTION_MOVE = {ACTION_UP : (-1, 0),
               ACTION_DOWN : (1, 0),
               ACTION_LEFT : (0, -1),
               ACTION_RIGHT : (0, 1)}


class Environment:
    def __init__(self, theMap):
        self.__states = theMap
        self.__reward_wall = -5

    def do(self, state, action):
        move = ACTION_MOVE[action]
        new_state = (state[0] + move[0], state[1] + move[1])

        if new_state not in self.__states \
           or arcade.check_for_collision_with_list(new_state, self.__state):
            reward = self.__reward_wall
        else:
            state = new_state
            reward = REWARD_DEFAULT

        return state, reward

    @property
    def states(self):
        return list(self.__states.keys())

    @property
    def start(self):
        return self.__start

    @property
    def height(self):
        return self.__rows

    @property
    def width(self):
        return self.__cols
    


class MazeWindow(arcade.Window):
    def __init__(self, agent1, agent2):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "TRON HERITAGE")
        self.__agent1 = agent1
        self.__agent2 = agent2

        self.__obstacles = arcade.SpriteList()
        self.__j1 = arcade.Sprite('boxBlue.png', SPRITE_SCALE)
        self.__j2 = arcade.Sprite('boxRed.png', SPRITE_SCALE)

        self.__j1.center_x, self.__j1.center_y = SCREEN_WIDTH / 2 + 20, SCREEN_HEIGHT / 2
        self.__j2.center_x, self.__j2.center_y = SCREEN_WIDTH / 2 - 20, SCREEN_HEIGHT / 2

        self.__j1direction_x, self.__j1direction_y = SPRITE_OFFSET, 0
        self.__j2direction_x, self.__j2direction_y = - SPRITE_OFFSET, 0

        self.__win = 0

        

    def on_draw(self):
        arcade.start_render()
        self.__j1.draw()
        self.__j2.draw()
        self.__obstacles.draw()

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
    

    def state_to_xyj1(self, state):
        return self.__j1.center_x + self.__j1direction_x, self.__j1.center_y + self.__j1direction_y

    def on_update(self, delta_time: float):
        self.__obstacles.append(self.__j1)
        self.__obstacles.append(self.__j2)

        self.__agent1.step()
        j1Next = arcade.Sprite('boxBlue.png', SPRITE_SCALE)
        j1Next.center_x, j1Next.center_y = self.state_to_xyj1(self.__agent1.state)
        self.__j1 = j1Next

        self.__agent2.step()
        j2Next = arcade.Sprite('boxRed.png', SPRITE_SCALE)
        j2Next.center_x, j2Next.center_y = self.__j2.center_x + self.__j2direction_x, self.__j2.center_y + self.__j2direction_y 
        self.__j2 = j2Next
        
        if arcade.check_for_collision_with_list(self.__j2, self.__obstacles) or not self.isInside(self.__j2.center_x, self.__j2.center_y):
            print('j1 win')
            arcade.close_window()

        if arcade.check_for_collision_with_list(self.__j1, self.__obstacles) or not self.isInside(self.__j1.center_x, self.__j1.center_y):
            print('j2 win')
            arcade.close_window()


    def isInside(self, x, y):
        return x >= 0 and x < SCREEN_WIDTH and y >= 0 and y < SCREEN_HEIGHT    


class Agent:
    def __init__(self, env, alpha = 1, gamma = 0.6, cooling_rate = 0.999):
        self.__qtable = {}
        for state in env.states:
            self.__qtable[state] = {}
            for action in ACTIONS:
                self.__qtable[state][action] = 0.0
        
        self.__env = env
        self.__alpha = alpha
        self.__gamma = gamma
        self.__history = []
        self.__cooling_rate = cooling_rate


    def best_action(self):
        # if random() < self.__temperature:
        #     self.__temperature *= self.__cooling_rate
        #     return choice(ACTIONS)
        # else:
        q = self.__qtable[self.__state]
        return max(q, key = q.get)

    def step(self):
        action = self.best_action()
        state, reward = self.__env.do(self.__state, action)
        
        maxQ = max(self.__qtable[state].values())
        delta = self.__alpha * (reward + self.__gamma * maxQ - self.__qtable[self.__state][action])
        self.__qtable[self.__state][action] += delta
        
        self.__state = state
        self.__score += reward
        return action, reward

    
    @property
    def state(self):
        return self.__state

    @property
    def score(self):
        return self.__score

    @property
    def environment(self):
        return self.__env



if __name__ == '__main__':
    window = MazeWindow()
    arcade.run()