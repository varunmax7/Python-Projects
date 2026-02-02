#Week-9 P1
#Draw point
import turtle
turtle.setup(500, 500)
pen = turtle.Turtle()
def drawpoint(x, y, color, size):
    pen.pencolor(color)
    pen.pensize(size)
    pen.up()
    pen.goto(x,y)
    pen.down()
    pen.dot()
    pen.penup()
drawpoint(0, 0, 'red', 5)
pen.hideturtle()
turtle.done()
