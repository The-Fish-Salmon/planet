from main import System, Star, Planet
import turtle

system = System(width=1100, length=850)
star = Star(system, mass=10000)
planet = Planet(system, mass=1, position=(-400, 0), velocity=(0, 5))

while True:
    system.gravity_acc(star, planet)
    system.update()