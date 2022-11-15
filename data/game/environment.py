from envi import ACTION_MOVE, START_J1, START_J2, ACTION_UP, ACTION_DOWN, ACTION_LEFT, ACTION_RIGHT, SPRITE_OFFSET, SCREEN_WIDTH, SCREEN_HEIGHT
from data.game.pos import Pos
import arcade

class Environment:
    def __init__(self):
        self.__j1 = Pos(SCREEN_WIDTH / 2 + START_J1[0], SCREEN_HEIGHT / 2 + START_J1[1])
        self.__j2 = Pos(SCREEN_WIDTH / 2 + START_J2[0], SCREEN_HEIGHT / 2 + START_J2[1])

        self.__obstacles = list()

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
            

    def do(self, action):
        direction =  ACTION_MOVE[action]

        nextPos = Pos(self.__j1.x + direction[0], self.__j1.y + direction[1])

        nextRadar = self.update_radar(nextPos)

        radarState = self.get_radar_state(nextRadar)

        if self.check_collision_with_obstacles(nextPos) and self.is_inside(nextPos):
            reward = -2 * 2**9

        
        
        return radarState, 0

    
    def get_radar_state(self, radar):
        state = ""
        for case in radar:
            if self.check_collision_with_obstacles(case) or not self.is_inside(case):
                state += "1"
            else:
                state += "0"
        return state

    def check_collision(self, pos1, pos2):
        if (pos1.x > pos2.x and pos1.x < pos2.x + SPRITE_OFFSET) and (pos1.y > pos2.y and pos1.y < pos2.y + SPRITE_OFFSET):
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


