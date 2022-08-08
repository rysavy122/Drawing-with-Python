import turtle
import random
import time

turtle.tracer(0, 0)
turtle.hideturtle()


t = turtle.Pen()
c = turtle.Screen()


c.bgcolor("white")
t.color('yellow','brown')
t.begin_fill()

#loops = 0

# Mandala
for x in range(1,361):  
    t.forward(150)
    t.left(225)
    t.forward(300)
    t.left(25)
    t.forward(250)
    t.left(225)
    t.forward(200)
    t.left(25)
    t.forward(100)
    t.left(15)
    t.forward(150)
    t.hideturtle()    
    #loops = loops+1
    #print('Loops:' + str(loops))

print("\nProzess beendet, Mandala fertig!\n")

t.end_fill()
turtle.update()
