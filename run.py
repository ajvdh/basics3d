import pyglet


from version_004.game import ui

main_window = ui.MyWindow(1280, 720, "My Pyglet Window", resizable=True)
pyglet.app.run()
