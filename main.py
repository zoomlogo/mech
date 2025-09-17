from pyglet.math import *
import pyglet

import ball

class GameWindow(pyglet.window.Window):
    GRAVITY = Vec2(0, -9.80667)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # game states
        self.is_paused = False

        # simulated objects
        self.bodies = []

        # internal stuff
        self.batch = pyglet.graphics.Batch()

    def add_body(self, body):
        body.assign_batch(self.batch)
        self.bodies.append(body)

    def on_draw(self):
        # draw everything we need
        self.clear()
        self.update_all_drawables()
        self.batch.draw()

    def update(self, dt):
        # update all game objects
        for body in self.bodies:
            body.apply_forces(body.m * GameWindow.GRAVITY)
            body.update(dt)

    def update_all_drawables(self):
        # update all positions / whatever of all drawables
        for body in self.bodies:
            body.update_shape()

if __name__ == "__main__":
    win = GameWindow(1024, 512, "2D Mechanics Simulation")
    win.add_body(ball.Ball(Vec2(512, 256)))

    # run update
    pyglet.clock.schedule_interval(win.update, 1 / 120)

    # display the window and run the app
    pyglet.app.run()
