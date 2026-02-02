# Week 9– Program 3 # Draw Circle
import turtle
class circle:
    def __init__(self, radius):
        self.radius=radius
    def draw_circle(self):
        cir=turtle.Turtle()
        print(cir.circle(self.radius))
        cir.hideturtle()
        turtle.done()
p=circle(int(input('enter radius: ')))

p.draw_circle()


