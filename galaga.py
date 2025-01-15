import pgzrun
import random

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

WIDTH = 500
HEIGHT = 400

ship = Actor("galaga")

ship.x = WIDTH//2
ship.y = HEIGHT-50

speed = 4

bullets = []
enemies = []

enemies.append(Actor("bug1"))
enemies[-1].x=10
enemies[-1].y=-100

def on_key_down(key):
    if key== keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y-50       

def update():
    if keyboard.left:
        ship.x  -= 4
        if ship.x<0:
            ship.x = WIDTH//2
    if keyboard.right:
        ship.x += 4
        if ship.x>WIDTH:
            ship.x = WIDTH//2
    for bullet in bullets:
        if bullet.y <=0:
            bullets.remove(bullet)
        else:
            bullet.y -=10
    for bug in enemies:
        bug.y += 5
        if bug.y >= HEIGHT:
            bug.y = -100
            bug.x = random.randint(50,WIDTH-50)

def draw():
    screen.clear()
    screen.fill(BLUE)
    for bullet in bullets:
        bullet.draw()
    for bug in enemies:
        bug.draw()
    ship.draw()

pgzrun.go()