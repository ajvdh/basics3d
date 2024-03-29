import pyglet
from version_001.game import mouse
from version_001.game import load


window = pyglet.window.Window()

score_label = pyglet.text.Label(text="Score: 0", x=10, y=460)
level_label = pyglet.text.Label(text="My Amazing Game",
                                x=window.width // 2, y=window.height // 2, anchor_x='center')


players = load.asteroids(3)


def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


@window.event
def on_key_press(symbol, modifiers):
    print('A key was pressed')


@window.event
def on_draw():
    # draw things here
    window.clear()

    level_label.draw()
    score_label.draw()

    for player in players:
        player.draw()



def main():
    print("python main function")
    pyglet.app.run()


if __name__ == '__main__':
    main()

