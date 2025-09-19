from pyglet.math import *
import pyglet

import ball

class MainWindow(pyglet.window.Window):
    # some constants
    GRAVITY = Vec2(0, -9.80667)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # game states
        self.is_paused = False

        # simulated objects
        self.bodies = set()

        # internal stuff
        self.batch = pyglet.graphics.Batch()
        self.debug_batch = pyglet.graphics.Batch()

        # debug stuff
        self.debug = True
        self.net_energy_label = pyglet.text.Label(
            'Total Energy = 0 J',
            font_size=12,
            x=2, y=self.height,
            anchor_y='top', batch=self.debug_batch
        )

    def on_draw(self):
        # clear screen and draw everything
        self.clear()
        self.update_all_drawables()
        self.batch.draw()
        if self.debug: self.debug_batch.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.F3:
            self.debug = not self.debug


    def update(self, dt):
        # update all game objects
        for body in self.bodies:
            body.apply_forces(body.m * self.GRAVITY)
            body.update(dt)
            body.border_collide(self.width, self.height)

    def update_all_drawables(self):
        # update all positions / whatever of all drawables
        energy = 0
        for body in self.bodies:
            body.update_shape()
            energy += body.m * body.v.length_squared() / 2  # Kinetic Energy
            energy += body.m * body.x.y * -self.GRAVITY.y  # Potential Energy

        if not self.debug: return  # dont update debugging items if debug mode is off

        self.net_energy_label.text = f'Total Energy = {energy:.6f} J.'

    def add_body(self, body):
        # add a rigidbody
        body.assign_batch(self.batch)
        self.bodies.add(body)


if __name__ == "__main__":
    win = MainWindow(1024, 512, "2D Mechanics Simulation")
    win.add_body(ball.Ball(Vec2(512, 256), radius=10, color=(123, 255, 120)))

    # run update
    pyglet.clock.schedule_interval(win.update, 1 / 60)

    # display the window and run the app
    pyglet.app.run()
