from main import System, Star, Planet,  SystemCelestialBody
import turtle

system = System(width=1100, length=850)
star = Star(system, mass=10000)
planets = (Planet(system, mass=1, position=(-300, 0), velocity=(0, 5), radius = 1),
           Planet(system, mass=2, position=(400, 0), velocity=(0, -4),radius = 1),
           Planet(system, mass=10, position=(500, 0), velocity=(0, -4),radius = 1)
           )

while True:
    system.all_interactions()
    system.update()