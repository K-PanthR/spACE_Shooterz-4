import pgzrun
import random

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

WIDTH = 850
HEIGHT = 600

ship = Actor("galaga")

ship.x = WIDTH//2
ship.y = HEIGHT-50

speed = 50

score=0

ship.dead = False
ship.countdown = 90

def ship_gameover():
    screen.fill("Blue")
    screen.draw.text("Time Up! You Scored "+str(score), midtop=(WIDTH/2,10),fontsize=40)

direction = 1

bullets = []
enemies = []

def display_score():
    screen.draw.text("Score:"+str(score), color="black", topleft=(10,10))

for x in range(8):
   for y in range(5):
       enemies.append(Actor("bug1"))
       enemies[-1].x = 100 + 80 * x
       enemies[-1].y = 80 + 50 * y 

def on_key_down(key):
    if ship.dead == False:
        if key== keys.SPACE:
            bullets.append(Actor("bullet"))
            bullets[-1].x = ship.x
            bullets[-1].y = ship.y-50       

def update():
    global score
    global direction
    move_down = False 

    if ship.dead == False:
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
    
    if len(enemies) == 0:
        ship_gameover()

    if len(enemies) > 0 and (enemies[-1].x > WIDTH - 80 or enemies[0].x < 80):
        move_down = True
        direction = direction*-1
    
    for enemy in enemies:
        enemy.x += 5 * direction
        enemy.y += 0.5
        if move_down == True:
            enemy.y += 20
        if enemy.y >= 500:
            enemies.remove(enemy)
        
        for bullet in bullets:
            if enemy.colliderect(bullet):
                sounds.find_money.play()  
                bullets.remove(bullet)
                enemies.remove(enemy)
                score  += 100
                if len(enemies) == 0:
                    ship_gameover()
        
        if enemy.colliderect(ship):
            ship.dead = True
    
    if ship.dead:
        ship.countdown -= 1
    if ship.countdown == 0:
        ship.dead = False
        ship.countdown = 90

def draw():
    screen.clear()
    screen.fill(BLUE)
    screen.blit("starry_sky" , (0,0))
    for bullet in bullets:
        bullet.draw()
    for bug in enemies:
        bug.draw()
    if ship.dead == False:
        ship.draw()
    display_score()
    if len(enemies) == 0:
        ship_gameover() 

pgzrun.go()