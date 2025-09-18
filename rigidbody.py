# rigidbody parent class implementation
from pyglet.math import *

class RigidBody:
    # parent class to derieve from
    def __init__(self,
        x,                       # [m] position
        mass  = 1,               # [kg] mass
        L     = 1,               # [kg m²] moment of interia
        v0    = Vec2(),          # [m s⁻¹] initial velocity
        θ     = 0,               # [rad] angular position
        ω0    = 0,               # [rad s⁻¹] initial angular velocity
        color = (255, 255, 255), # color; white
        batch = None, *args, **kwargs
    ):
        # kinetics
        self.x  = x  # [m] position
        self.v  = v0 # [m s⁻¹] velocity
        self.a  = 0  # [m s⁻²] acceleration

        self.Θ  = 0  # [rad] angular position
        self.ω  = ω0 # [rad s⁻¹] angular velocity
        self.α  = 0  # [rad s⁻²] angular acceleration

        self.m   = mass     # [kg] mass
        self.m_i = 1 / mass # [kg⁻¹] reciprocal of mass
        self.L   = L        # [kg m²] moment of interia
        self.L_i = 1 / L    # [kg⁻¹ m⁻²] reciprocal of moment of interia

        # properties
        # self.cor = 1  # coefficient of restitution

        self.color = color
        self.shape = None  # note: change this to the shape in inherited class

    def assign_batch(self, batch):
        self.shape.batch = batch

    def apply_forces(self,
        *forces, # [N] the forces to apply
    ):
        if not forces: return
        # find net force and add
        self.a = self.a + self.m_i * sum(forces)

    def apply_torques(self,
        *torques, # [N m] the torques to apply
    ):
        if not torques: return
        self.α = self.α + self.L_i * sum(torques)


    def update(self,
        dt, # [s] tiny change in time
    ):
        # velocity verlet integration
        self.x = self.x + self.v * dt + self.a * dt**2 / 2
        self.v = self.v + self.a * dt

        # reset acceleration
        self.a = Vec2()


    # NotImplemented stuff, the children should implement it
    rigidbody_collide = border_collide = update_shape = lambda self: 1 / 0  # divide by zero to raise exception lol
