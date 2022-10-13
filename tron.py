import arcade



SPRITE_SCALE = 0.01
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SPRITE_OFFSET = 6

class TronWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "TRON HERITAGE")
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
            print('j2 win')
            arcade.close_window()
        
        if arcade.check_for_collision_with_list(self.__j2, self.__obstacles) or not self.isInside(self.__j2.center_x, self.__j2.center_y):
            print('j1 win')
            arcade.close_window()

    def isInside(self, x, y):
        return x >= 0 and x < SCREEN_WIDTH and y >= 0 and y < SCREEN_HEIGHT    





if __name__ == '__main__':
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "TRON HERITAGE")
    tronView = TronWindow()
    window.show_view(tronView)
    arcade.run()