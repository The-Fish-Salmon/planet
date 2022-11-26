import math
import turtle

class SystemCelestialBody (turtle.Turtle):
    #An object that is used to give parameters to celestial bodies
    def __int__(self,system,mass,position=(0,0),velocity=(0,0)):
        # initialize body with parameters
        super(SystemCelestialBody, self).__init__()
        # Found it online, don't exactly know what it do
        # I use it instead of a bunch of trash code that didn't work
        # it let the bodies that we give parameters to take it
        self.mass = mass
        self.setposition(position)
        self.velocity =velocity
        # set parameters
        self.display_size = math.log(self.mass, 10)
        # set display size of stuff, if just mass it too big so log
        self.penup()
        self.hideturtle()
        # for drawing
        system.addstuff(self)
        #add the stuff to the system
    def draw(self):
        self.dot(self.display_size)
        #draw stuff
class System:
    #Create an object for the system and interation og stuff
    def __int__(self,width,length):
        # initialize system with width and length
        self.system = turtle.Screen()
        # Give it a background
        self.system.tracer(0)
        # needed to draw stuff
        self.system.setup(width,length)
        self.system.bgcolor("black")
        # parameters for background
        self.stuffs = []
        #list of stuff in the system

    def addstuff(self, stuff):
        self.stuffs.append(stuff)

    def delstuff(self, stuff):
        self.stuffs.remove(stuff)
        
class Star (SystemCelestialBody):
#Star object

class Planet (SystemCelestialBody):
#Planet object
