#pythone file to create a tree like structure
#using turtle module in python


import turtle
abhi = turtle.Turtle()
scr=turtle.Screen()
#putting color
scr.bgcolor('black')
abhi.pencolor('white')
#for more speed and adjusting
abhi.left(90)
abhi.speed(0)
abhi.penup()
abhi.goto(0,-200)
abhi.pendown()
#main 
def tree(i):
    if(i<10):
        return
    else:
        abhi.forward(i)
        abhi.left(30)
        tree(3*i/4)
        abhi.right(60)
        tree(3*i/4)
        abhi.left(30)
        abhi.backward(i)        
        
tree(100)
turtle.done()