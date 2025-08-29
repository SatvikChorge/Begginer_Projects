import turtle
import colorsys

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

n = 36
colors = [colorsys.hsv_to_rgb(i/n, 1, 1) for i in range(n)]

for i in range(300):
    t.color(colors[i % n])
    t.circle(i, 60)
    t.left(20)
    t.forward(20)

turtle.done()
