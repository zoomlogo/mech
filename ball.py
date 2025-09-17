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
