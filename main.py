import turtle
import math
import random
from playsound import playsound

#Set up screen
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Space Shooter")
wn.bgpic("Background.png")

#Register the shapes
turtle.register_shape("enemy.gif")
turtle.register_shape("player1.gif")
turtle.register_shape("bullet.gif")
turtle.register_shape("explosion.gif")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("Purple")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range (4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Set score
score = 0
    #Draw Score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("White")
score_pen.penup()
score_pen.setposition(-295,275)
scorestring ="Score: %s" %score
score_pen.write(scorestring,False,align="left",font=("Ariel",14,"normal"))
score_pen.hideturtle()

#create player
player = turtle.Turtle()
player.color("blue")
player.shape("player1.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
playerspeed=15

#create explosion
explosion = turtle.Turtle()
explosion.color("red")
explosion.shape("explosion.gif")
explosion.penup()
explosion.speed(0)
explosion.hideturtle()

#Choose a number of enemies
number_of_enemies = 5
enemies = []
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color("red")
    enemy.shape("enemy.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x,y)

#Create player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("bullet.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bulletspeed = 40
#define bullet state
#ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"

def fire_bullet():
    global bulletstate
    if bulletstate =="ready":
        bulletstate = "fire"
        #Move the bullet to the just above the player
        x = player.xcor()
        y=player.ycor() + 15
        bullet.setposition(x,y)
        bullet.showturtle()
        playsound("laser.wav",block = False)

#Collison between two objects
def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 24:
        return True
    else:
        return False

#Moving player right and left
def move_left():
    x = player.xcor()
    x = x-playerspeed
    if player.xcor()<-280:
        x=-280
    player.setx(x)


def move_right():
    x = player.xcor()
    x = x+playerspeed
    if player.xcor()>280:
        x=280
    player.setx(x)


#Keyboard bidings
turtle.listen()
turtle.onkeypress(move_left,"Left")
turtle.onkeypress(move_right,"Right")
turtle.onkey(fire_bullet,"space")


#------------------------------------------------------------------------------
#Main game loop
enemyspeed = 2
def main_game_loop():
    global enemyspeed
    global bulletstate
    global score
    while True:
        explosion.hideturtle()
        #Move the enemy
        for enemy in enemies:

            x= enemy.xcor()
            x+=enemyspeed
            enemy.setx(x)
            #Move the enemy back and forth
            if enemy.xcor()>280:
                for e in enemies:
                    y = e.ycor()
                    y-=40
                    e.sety(y)
                enemyspeed *=-1

            if enemy.xcor()<-280:
                for e in enemies:
                    y = e.ycor()
                    y-=40
                    e.sety(y)
                enemyspeed *=-1
            if enemy.ycor()<-290:
                print("Game over")
                return True
            #Check collision between the bullet and the enemy
            if isCollision(bullet,enemy):
                explosion.setx(enemy.xcor())
                explosion.sety(enemy.ycor())
                explosion.showturtle()
                #Reset the bullet
                bullet.hideturtle()
                bulletstate = "ready"
                bullet.setposition(0,-400)
                #Reset enemy position
                x = random.randint(-200,200)
                y = random.randint(200,250)
                enemy.setposition(x,y)
                #Update score
                score +=10
                scorestring ="Score: %s" %score
                score_pen.clear()
                score_pen.write(scorestring,False,align="left",font=("Ariel",14,"normal"))
                playsound("explosion.wav",block = False)
                enemyspeed*=1.2

            if isCollision(player,enemy):
                player.hideturtle()
                enemy.hideturtle()
                print("Game Over")
                return True
        #Move the bullet
        if bulletstate=="fire":
            y = bullet.ycor()
            y+=bulletspeed
            bullet.sety(y)
        #Check if the bullet reach the end
        if bullet.ycor()>280:
            bullet.hideturtle()
            bulletstate="ready"
#------------------------------------------------------------------------------
main_game_loop()
