from pyglet.math import *
import pyglet

from rigidbody import RigidBody

class Box(RigidBody):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # box dimensions
        self.size = kwargs.get("size", Vec2(10, 10))
        self.shape = pyglet.shapes.Box(*self.x, *self.size, color=self.color)

    def update_shape(self):
        self.shape.x, self.shape.y = self.x

    def border_collide(self, width, height):
        raise NotImplementedError

    def rigidbody_collide(self):
        raise NotImplementedError

    def box_collide(self, other):
        raise NotImplementedError
