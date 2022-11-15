import arcade
from envi import WINNER, SCREEN_HEIGHT, SCREEN_WIDTH, SPRITE_OFFSET, RADAR_SIZE, BIKE_J1, BIKE_J2, RADAR_DISPLAY, ACTION_MOVE, ACTION_UP, ACTION_DOWN, ACTION_LEFT, ACTION_RIGHT
import data.game.environment as env

class TronWindow(arcade.View):
    def __init__(self, agentJ1, agentJ2, env):
        super().__init__()
        self.__agentJ1 = agentJ1
        self.__agentJ2 = agentJ2
        self.__env = env

        self.__lastWinner = "None"

        self.__j1 = arcade.Sprite(BIKE_J1, image_height=SPRITE_OFFSET, image_width=SPRITE_OFFSET)
        self.__j2 = arcade.Sprite(BIKE_J2, image_height=SPRITE_OFFSET, image_width=SPRITE_OFFSET)

        self.reset()

    
    def init_radar_display(self, radar):
        radarDisplay = arcade.SpriteList()
        for case in radar:
            radarCase = arcade.Sprite(RADAR_DISPLAY, image_height=10, image_width=10)
            radarCase.center_x, radarCase.center_y = case.x, case.y
            radarDisplay.append(radarCase)


        return radarDisplay


    def on_draw(self):
        
        arcade.start_render()
        self.__obstacles.draw()
        self.__j1Radar.draw()
        self.__j2Radar.draw()
        arcade.draw_text(f'J1 Iteration: {self.__agentJ1.getStep} - J2 Iteration: {self.__agentJ2.getStep} - Last Winner: {self.__lastWinner}',
                         10, 10,
                         arcade.csscolor.WHITE, 20)


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
        
        
        directionJ1 = self.__agentJ1.best_action()
        directionJ2 = self.__agentJ2.best_action()
        stateJ1, stateJ2, rewardJ1, rewardJ2, winner = self.__env.step(directionJ1, directionJ2)
        self.__agentJ1.step(stateJ1, rewardJ1)
        self.__agentJ2.step(stateJ2, rewardJ2)

        j1Next = arcade.Sprite(BIKE_J1, image_height=10, image_width=10)
        j1Next.center_x, j1Next.center_y = self.__env.j1.x, self.__env.j1.y
        self.__j1 = j1Next

        j2Next = arcade.Sprite(BIKE_J2, image_height=10, image_width=10)
        j2Next.center_x, j2Next.center_y = self.__env.j2.x, self.__env.j2.y
        self.__j2 = j2Next

        self.__j1Radar = self.init_radar_display(self.__env.j1Radar)
        self.__j2Radar = self.init_radar_display(self.__env.j2Radar)

        self.__obstacles.append(self.__j1)
        self.__obstacles.append(self.__j2)
        
        if winner != 0:
            self.__lastWinner = WINNER[winner]
            self.reset()

    def reset(self):
        self.__env.reset()
        self.__agentJ1.reset()
        self.__agentJ2.reset()

        self.__obstacles = arcade.SpriteList()

        self.__j1.center_x, self.__j1.center_y = self.__env.j1.x, self.__env.j1.y
        self.__j2.center_x, self.__j2.center_y = self.__env.j2.x, self.__env.j2.y

        self.__obstacles.append(self.__j1)
        self.__obstacles.append(self.__j2)

