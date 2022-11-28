from main import System, Star, Planet
import turtle

system = System(width=1080, length=720)
star = Star(system, mass=100000000)
planet = Planet(system, mass=100, position=(-400, 0), velocity=(1, 0))

while True:
    system.update()