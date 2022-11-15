from envi import ACTION_MOVE, START_J1, START_J2, ACTION_UP, ACTION_DOWN, ACTION_LEFT, ACTION_RIGHT, SPRITE_OFFSET, SCREEN_WIDTH, SCREEN_HEIGHT, LEN_STATE
from data.game.pos import Pos
import arcade

class Environment:
    def __init__(self):
        self.reset()

    def reset(self):
        self.__j1 = Pos(SCREEN_WIDTH / 2 + START_J1[0], SCREEN_HEIGHT / 2 + START_J1[1])
        self.__j2 = Pos(SCREEN_WIDTH / 2 + START_J2[0], SCREEN_HEIGHT / 2 + START_J2[1])

        self.__obstacles = list()

        self.__j1Radar = Pos(self.__j1.x, self.__j1.y)
        self.__j2Radar = Pos(self.__j2.x, self.__j2.y)

        self.__obstacles.append(self.__j1)
        self.__obstacles.append(self.__j2)

    
    def update_radar(self, player):
        radar = []

        case1 = Pos(player.x, player.y)
        case2 = Pos(player.x + SPRITE_OFFSET, player.y)
        case3 = Pos(player.x - SPRITE_OFFSET, player.y)
        case4 = Pos(player.x, player.y + SPRITE_OFFSET)
        case5 = Pos(player.x + SPRITE_OFFSET, player.y + SPRITE_OFFSET)
        case6 = Pos(player.x - SPRITE_OFFSET, player.y + SPRITE_OFFSET)
        case7 = Pos(player.x, player.y - SPRITE_OFFSET)
        case8 = Pos(player.x + SPRITE_OFFSET, player.y - SPRITE_OFFSET)
        case9 = Pos(player.x - SPRITE_OFFSET, player.y - SPRITE_OFFSET)

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
            

    def step(self, actionJ1, actionJ2):
        directionJ1 =  ACTION_MOVE[actionJ1]
        directionJ2 =  ACTION_MOVE[actionJ2]
        rewardJ1 = 0
        rewardJ2 = 0
        winner = 0


        self.__j1 = Pos(self.__j1.x + directionJ1[0], self.__j1.y + directionJ1[1])
        self.__j2 = Pos(self.__j2.x + directionJ2[0], self.__j2.y + directionJ2[1])

        self.__j1Radar = self.update_radar(self.__j1)
        self.__j2Radar = self.update_radar(self.__j2)

        radarStateJ1 = self.get_radar_state(self.__j1Radar)
        radarStateJ2 = self.get_radar_state(self.__j2Radar)
        

        if not self.check_collision(self.__j1, self.__j2):
            if self.check_collision_with_obstacles(self.__j1) or not self.is_inside(self.__j1):
                rewardJ1 = -2 * LEN_STATE
                rewardJ2 = LEN_STATE
                winner = 2
            if self.check_collision_with_obstacles(self.__j2) or not self.is_inside(self.__j2):
                rewardJ2 = -2 * LEN_STATE
                rewardJ1 = LEN_STATE
                reset = 1
        else:
            rewardJ1 = -2 * LEN_STATE
            rewardJ2 = -2 * LEN_STATE
            reset = 3

        self.__obstacles.append(self.__j1)
        self.__obstacles.append(self.__j2)

        # print("Radars : ", radarStateJ1, radarStateJ2)
        
        return radarStateJ1, radarStateJ2, rewardJ1, rewardJ2, winner


    
    
    def get_radar_state(self, radar):
        state = ""
        for case in radar:
            if self.check_collision_with_obstacles(case) or not self.is_inside(case):
                state += "1"
            else:
                state += "0"
        return state

    def check_collision(self, pos1, pos2):
        if (pos1.x < pos2.x + SPRITE_OFFSET and pos1.x + SPRITE_OFFSET > pos2.x) and (pos1.y < pos2.y + SPRITE_OFFSET and pos1.y + SPRITE_OFFSET > pos2.y):
            return True
        return False
    
    def check_collision_with_obstacles(self, pos):
        for obstacle in self.__obstacles:
            if self.check_collision(pos, obstacle):
                return True

    def is_inside(self, pos):
        if pos.x > 0 and pos.x < SCREEN_WIDTH and pos.y > 0 and pos.y < SCREEN_HEIGHT:
            return True
        return False

    @property
    def j1(self):
        return self.__j1
    
    @property
    def j2(self):
        return self.__j2
    
    @property
    def j1Radar(self):
        return self.__j1Radar
    
    @property
    def j2Radar(self):
        return self.__j2Radar


