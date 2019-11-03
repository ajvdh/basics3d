import pyglet


def on_mouse_motion(x, y, dx, dy):
    pass


def on_mouse_press(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT:
        print('LEFT pressed')
    if button == pyglet.window.mouse.MIDDLE:
        print('MIDDLE pressed')
    if button == pyglet.window.mouse.RIGHT:
        print('RIGHT pressed')
    pass


def on_mouse_release(x, y, button, modifiers):
    pass


def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    pass