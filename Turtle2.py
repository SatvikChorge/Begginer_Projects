import turtle

t = turtle.Turtle()
t.speed(16)

for i in range(96):
    t.forward(i * 5)
    t.left(120)

turtle.done()
