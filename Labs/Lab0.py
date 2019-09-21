import turtle

screen = turtle.Screen()
screen.bgcolor("#90ee90")
t = turtle.Turtle()
t.pensize(5)
t.shape('turtle')
t.color("blue")
t.stamp()

for _ in range(12):
    t.penup()
    t.forward(100)
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(20)
    t.pendown()
    t.stamp()
    t.penup()
    t.backward(130)
    t.left(30)

screen.exitonclick()
# the pensize (thickness) = 5
# from center to the tick = 100
# the length of the tick  = 10
# from the tick to turtle = 10




