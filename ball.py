from pyglet.math import *
import pyglet

from rigidbody import RigidBody

class Ball(RigidBody):
    #rigidbody_collide = border_collide
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # circle shape stuff
        self.radius = kwargs.get("radius", 20)
        self.shape = pyglet.shapes.Circle(*self.x, self.radius, color=self.color)

    def update_shape(self):
        self.shape.x, self.shape.y = self.x

    def border_collide(self, width, height):
        # compute the extreme points of the circle
        leftmost = self.x.x - self.radius
        rightmost = self.x.x + self.radius
        topmost = self.x.y + self.radius
        bottommost = self.x.y - self.radius

        # flip velocity if required
        if leftmost <= 0 or rightmost >= width:
            self.v = Vec2(-self.v.x, self.v.y)

        if bottommost <= 0 or topmost >= height:
            self.v = Vec2(self.v.x, -self.v.y)

    def rigidbody_collide(self, other):
        if isinstance(other, Ball):
            self.ball_collide(other)

    def ball_collide(self, other):
        pass
