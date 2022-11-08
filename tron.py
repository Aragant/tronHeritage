import arcade



SPRITE_SCALE = 0.02
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SPRITE_OFFSET = 10.5

ACTION_UP = 'U'
ACTION_DOWN = 'D'
ACTION_LEFT = 'L'
ACTION_RIGHT = 'R'
ACTIONS = [ACTION_UP, ACTION_DOWN, ACTION_LEFT, ACTION_RIGHT]


class Agent:
    def __init__(self, alpha = 1, gamma = 0.6, cooling_rate = 0.999):
        # self.__env = env
        self.__alpha = alpha
        self.__gamma = gamma
        self.__cooling_rate = cooling_rate

        self.__qTable = {}


        states = self.init_states()


        for state in states:
            self.__qTable[state] = {}
            for action in ACTIONS:
                self.__qTable[state][action] = 0.0

        print(self.__qTable)

    def init_states(self):
        states = []
        radarSize = 9

        for i in range(1, 2**radarSize):
            states.append(bin(i)[2:].zfill(radarSize))
            
        # print(states)
        return states

class TronWindow(arcade.View):
    def __init__(self):
        super().__init__()
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
    
    def on_update(self, delta_time: float):
        self.__obstacles.append(self.__j1)
        self.__obstacles.append(self.__j2)

        j1Next = arcade.Sprite('boxBlue.png', SPRITE_SCALE)
        j1Next.center_x, j1Next.center_y = self.__j1.center_x + self.__j1direction_x, self.__j1.center_y + self.__j1direction_y
        self.__j1 = j1Next

        j2Next = arcade.Sprite('boxRed.png', SPRITE_SCALE)
        j2Next.center_x, j2Next.center_y = self.__j2.center_x + self.__j2direction_x, self.__j2.center_y + self.__j2direction_y 
        self.__j2 = j2Next

        if arcade.check_for_collision_with_list(self.__j1, self.__obstacles) or not self.isInside(self.__j1.center_x, self.__j1.center_y):
            self.window.show_view(WinView("Red"))
        
        if arcade.check_for_collision_with_list(self.__j2, self.__obstacles) or not self.isInside(self.__j2.center_x, self.__j2.center_y):
            self.window.show_view(WinView("Blue"))

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
    agent = Agent()
    
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "TRON HERITAGE")
    tronView = TronWindow()
    window.show_view(tronView)
    arcade.run()