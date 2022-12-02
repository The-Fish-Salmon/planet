import math
import turtle
import numpy as np


class SystemCelestialBody(turtle.Turtle):
    # An object that is used to give parameters to celestial bodies
    def __init__(self, system, mass, position=(0, 0), velocity=(0, 0)):
        # initialize body with parameters
        super(SystemCelestialBody, self).__init__()
        # Found it online, don't exactly know what it do
        # I use it instead of a bunch of trash code that didn't work
        # it let the bodies that we give parameters to take it
        self.mass = mass
        self.setposition(position)
        self.velocity = velocity
        # set parameters
        self.display_size = max(math.log(self.mass, 1.1), 15)
        # set display size of stuff, if just mass it too big so log
        self.penup()
        self.hideturtle()
        # for drawing
        system.addstuff(self)
        # add the stuff to the system

    def draw(self):
        self.clear()
        self.dot(self.display_size)
        # draw stuff

    def move(self):
        self.setx(self.xcor() + self.velocity[0])
        self.sety(self.ycor() + self.velocity[1])


class System:
    """
    Create an object for the system and interation og stuff
    """
    def __init__(self, width, length):
        # initialize system with width and length
        self.system = turtle.Screen()
        # Give it a background

        self.system.tracer(n=3, delay=10)#speed
        # needed to draw stuff
        self.system.setup(width, length)
        self.system.bgcolor("black")
        # parameters for background
        self.stuffs = []
        # list of stuff in the system

    def addstuff(self, stuff):
        self.stuffs.append(stuff)

    def delstuff(self, stuff):
        self.stuffs.remove(stuff)

    def update(self):
        for stuff in self.stuffs:
            stuff.move()
            stuff.draw()
        self.system.update()

    def gravity_acc(self, stuff1: SystemCelestialBody, stuff2: SystemCelestialBody):
        force = stuff1.mass * stuff2.mass / (stuff1.distance(stuff2) ** 2)
        angle = stuff1.towards(stuff2)
        i = 1
        for stuffs in stuff1, stuff2:
            acceleration = force/stuffs.mass
            acc_x = acceleration*np.cos(np.radians(angle))
            acc_y = acceleration*np.sin(np.radians(angle))
            stuffs.velocity = (stuffs.velocity[0] + (i * acc_x), stuffs.velocity[1] + (i * acc_y))
            i = -1


class Star(SystemCelestialBody):
    # Star object
    def __init__(self, system, mass, position=(0, 0), velocity=(0, 0)):
        super().__init__(system, mass, position, velocity)
        self.color('orange')


class Planet(SystemCelestialBody):
    # Planet object
    def __init__(self, system, mass, position=(0, 0), velocity=(0, 0)):
        super().__init__(system, mass, position, velocity)
        self.color('blue')
