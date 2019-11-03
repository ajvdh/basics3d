import pyglet
from version_002.game import states
from pyglet.window import key



class MyWindow(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(800, 600, *args, **kwargs)
        self.game_state = states.GameStates.MAIN_MENU


    def on_draw(self):
        self.clear()

        if self.game_state == states.GameStates.MAIN_MENU:
            self.game_state = states.GameStates.PLAYING
            print(self.game_state)

        elif self.game_state == states.GameStates.PLAYING:
            self.game_state = states.GameStates.MAIN_MENU
            print(self.game_state)


    def on_key_press(self, symbol, modifiers):
        """ Handles key presses in/for menus and toggling fps display """
        print('key pressed')


    def on_mouse_motion(self, x, y, dx, dy):
        print(x, y)


