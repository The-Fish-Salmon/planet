from main import System, Star, Planet,  SystemCelestialBody
import turtle

system = System(width=1100, length=850)
star = Star(system, mass=10000)
planet1 = Planet(system, mass=1, position=(-300, 0), velocity=(0, 5),)

planet2 = Planet(system, mass=2, position=(400, 0), velocity=(0, -4),)

while True:
    system.gravity_acc(star, planet1)

    system.gravity_acc(star, planet2)
    system.gravity_acc(planet2, planet1)


    system.update()