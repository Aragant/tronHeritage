import arcade
from envi import SCREEN_HEIGHT, SCREEN_WIDTH, SPRITE_OFFSET, RADAR_SIZE, BIKE_J1, BIKE_J2, RADAR_DISPLAY

class TronWindow(arcade.View):
    def __init__(self, agentJ1, agentJ2):
        super().__init__()
        self.__agentJ1 = agentJ1
        self.__agentJ2 = agentJ2

    def setup(self):
        self.__obstacles = arcade.SpriteList()
        self.__j1 = arcade.Sprite(BIKE_J1, image_height=10, image_width=10)
        self.__j2 = arcade.Sprite(BIKE_J2, image_height=10, image_width=10)

        self.__j1.center_x, self.__j1.center_y = SCREEN_WIDTH / 2 + 20, SCREEN_HEIGHT / 2
        self.__j2.center_x, self.__j2.center_y = SCREEN_WIDTH / 2 - 20, SCREEN_HEIGHT / 2

        self.__j1direction_x, self.__j1direction_y = SPRITE_OFFSET, 0
        self.__j2direction_x, self.__j2direction_y = - SPRITE_OFFSET, 0

        self.__j1Radar = self.init_radar_display(self.__j1)
        self.__j2Radar = self.init_radar_display(self.__j2)

        self.__j1state = self.getRadarState(self.__j1Radar)
        self.__j2state = self.getRadarState(self.__j2Radar)

        print(self.__j1.height, self.__j1.width)

        self.__obstacles.append(self.__j1)
        self.__obstacles.append(self.__j2)

        self.__win = 0

    
    def init_radar_display(self, player):
        radar = []

        boxPath = RADAR_DISPLAY

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

        case10 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case10.center_x, case10.center_y = player.center_x - SPRITE_OFFSET * 2, player.center_y
        case11 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case11.center_x, case11.center_y = player.center_x + SPRITE_OFFSET * 2, player.center_y

        case12 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case12.center_x, case12.center_y = player.center_x - SPRITE_OFFSET * 2, player.center_y + SPRITE_OFFSET
        case13 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case13.center_x, case13.center_y = player.center_x + SPRITE_OFFSET * 2, player.center_y + SPRITE_OFFSET

        case14 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case14.center_x, case14.center_y = player.center_x - SPRITE_OFFSET * 2, player.center_y - SPRITE_OFFSET
        case15 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case15.center_x, case15.center_y = player.center_x + SPRITE_OFFSET * 2, player.center_y - SPRITE_OFFSET

        case16 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case16.center_x, case16.center_y = player.center_x, player.center_y - SPRITE_OFFSET * 2
        case17 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case17.center_x, case17.center_y = player.center_x - SPRITE_OFFSET, player.center_y - SPRITE_OFFSET * 2
        case18 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case18.center_x, case18.center_y = player.center_x + SPRITE_OFFSET, player.center_y - SPRITE_OFFSET * 2
        case19 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case19.center_x, case19.center_y = player.center_x - SPRITE_OFFSET * 2, player.center_y - SPRITE_OFFSET * 2
        case20 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case20.center_x, case20.center_y = player.center_x + SPRITE_OFFSET * 2, player.center_y - SPRITE_OFFSET * 2

        case21 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case21.center_x, case21.center_y = player.center_x, player.center_y + SPRITE_OFFSET * 2
        case22 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case22.center_x, case22.center_y = player.center_x - SPRITE_OFFSET, player.center_y + SPRITE_OFFSET * 2
        case23 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case23.center_x, case23.center_y = player.center_x + SPRITE_OFFSET, player.center_y + SPRITE_OFFSET * 2
        case24 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case24.center_x, case24.center_y = player.center_x - SPRITE_OFFSET * 2, player.center_y + SPRITE_OFFSET * 2
        case25 = arcade.Sprite(boxPath, image_height=RADAR_SIZE, image_width=RADAR_SIZE)
        case25.center_x, case25.center_y = player.center_x + SPRITE_OFFSET * 2, player.center_y + SPRITE_OFFSET * 2 

        radar.append(case1)
        radar.append(case2)
        radar.append(case3)
        radar.append(case4)
        radar.append(case5)
        radar.append(case6)
        radar.append(case7)
        radar.append(case8)
        radar.append(case9)
        radar.append(case10)
        radar.append(case11)
        radar.append(case12)
        radar.append(case13)
        radar.append(case14)
        radar.append(case15)
        radar.append(case16)
        radar.append(case17)
        radar.append(case18)
        radar.append(case19)
        radar.append(case20)
        radar.append(case21)
        radar.append(case22)
        radar.append(case23)
        radar.append(case24)
        radar.append(case25)

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

        j1Next = arcade.Sprite(BIKE_J1, image_height=10, image_width=10)
        j1Next.center_x, j1Next.center_y = self.__j1.center_x + self.__j1direction_x, self.__j1.center_y + self.__j1direction_y
        self.__j1 = j1Next

        j2Next = arcade.Sprite(BIKE_J2, image_height=10, image_width=10)
        j2Next.center_x, j2Next.center_y = self.__j2.center_x + self.__j2direction_x, self.__j2.center_y + self.__j2direction_y 
        self.__j2 = j2Next

        self.__j1Radar = self.init_radar_display(self.__j1)
        self.__j2Radar = self.init_radar_display(self.__j2)

        j1state = self.getRadarState(self.__j1Radar)
        j2state = self.getRadarState(self.__j2Radar)

        if arcade.check_for_collision(self.__j1, self.__j2) is not True:
            if arcade.check_for_collision_with_list(self.__j1, self.__obstacles) or not self.isInside(self.__j1.center_x, self.__j1.center_y):
                self.__agentJ1.updateReward(j1state, -2 * 2**9)
                self.__agentJ2.updateReward(j2state, 2**9)
                # self.__agentJ2.updateReward(j2state, 100)
                self.reset()
                # self.window.show_view(WinView("Red"))
            else:
                self.__agentJ1.updateReward(j1state, 0)


            if arcade.check_for_collision_with_list(self.__j2, self.__obstacles) or not self.isInside(self.__j2.center_x, self.__j2.center_y):
                # self.__agentJ1.updateReward(j1state, 100)
                self.__agentJ2.updateReward(j2state, -2 * 2**9)
                self.__agentJ1.updateReward(j1state, 2**9)
                self.reset()
                # self.window.show_view(WinView("Blue"))
            else:
                self.__agentJ2.updateReward(j2state, 0)


        else :
            self.__agentJ1.updateReward(j1state, -2 * 2**9)
            self.__agentJ2.updateReward(j2state, -2 * 2**9)
            self.reset()


        # if arcade.check_for_collision_with_list(self.__j1, self.__obstacles) or not self.isInside(self.__j1.center_x, self.__j1.center_y) \
        #     or arcade.check_for_collision_with_list(self.__j2, self.__obstacles) or not self.isInside(self.__j2.center_x, self.__j2.center_y) \
        #     or arcade.check_for_collision(self.__j1, self.__j2):
        #     self.reset()

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