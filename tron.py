import arcade
import os
import pickle

from data.game.game import TronWindow
from envi import ACTION_MOVE, SCREEN_HEIGHT, SCREEN_WIDTH, SPRITE_SCALE, SPRITE_OFFSET, RADAR_SIZE, ACTIONS, QTABLE_FILE_PATH_J1, QTABLE_FILE_PATH_J2, FILE_AGENT, GAME_NAME
from data.game.environment import Environment
from data.game.agent import Agent

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
    env = Environment()
    qTableJ1FilePath = QTABLE_FILE_PATH_J1
    qTableJ2FilePath = QTABLE_FILE_PATH_J2
    agentJ1 = Agent(env, qTableJ1FilePath)
    agentJ2 = Agent(env, qTableJ2FilePath)
    
    if os.path.exists(qTableJ1FilePath):
        agentJ1.load(qTableJ1FilePath)

    if os.path.exists(qTableJ2FilePath):
        agentJ2.load(qTableJ2FilePath)

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, GAME_NAME)
    tronView = TronWindow(agentJ1, agentJ2, env)

    window.show_view(tronView)
    arcade.run()

    agentJ1.save(qTableJ1FilePath)
    agentJ2.save(qTableJ2FilePath)