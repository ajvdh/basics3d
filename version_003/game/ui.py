import pyglet
from version_003.game.constants import MyColours as col
from version_003.game.constants import GameStates as stat
from pyglet.window import key


class Triangle:
    def __init__(self):
        self.vertices = pyglet.graphics.vertex_list(3, ('v3f', [-1.0, -0.5, 0.0, 0.5, -0.5, 0.0, 0.0, 0.5, 0.0]),
                                                    ('c3B', col.red + col.green + col.blue))

class Hex:
    def __init__(self):
        self.vertices = pyglet.graphics.vertex_list(4, ('v3f', [0.0, 0.0, 0.0, 0.0, 0.8, 0.0, 0.4, 0.4, 0.0, 0.4, -0.4, 0.0]),
                                                    ('c3B', col.red + col.green + col.blue + col.blue))
        # self.vertices = pyglet.graphics.vertex_list(3, ('v3f', [100.0, 100, 0, 100, 200, 0, 200, 200, 0]),
        #                                             ('c3B', col.red + col.green + col.blue))


class MyWindow(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)
        self.set_minimum_size(400, 300)
        pyglet.gl.glClearColor(0.0, 0.0, 0.0, 0.0)   # red, green, blue, alpha

        self.game_state = stat.MAIN_MENU

        self.triangle = Triangle()
        self.hex = Hex()


    def on_draw(self):
        self.clear()

        self.triangle.vertices.draw(pyglet.gl.GL_TRIANGLES)
        #self.hex.vertices.draw(pyglet.gl.GL_TRIANGLES)
        self.hex.vertices.draw(pyglet.gl.GL_QUADS)

        if self.game_state == stat.MAIN_MENU:
            self.game_state = stat.PLAYING
            print(self.game_state)

        elif self.game_state == stat.PLAYING:
            self.game_state = stat.MAIN_MENU
            print(self.game_state)

    def on_resize(self, width, height):
        pyglet.gl.glViewport(0, 0, width, height)

    def on_key_press(self, symbol, modifiers):
        """ Handles key presses in/for menus and toggling fps display """
        print('key pressed')


    def on_mouse_motion(self, x, y, dx, dy):
        print(x, y)


