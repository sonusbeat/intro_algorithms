import turtle

screen = turtle.Screen()
diego = turtle.Turtle()
diego.shape("turtle")

# how to draw a square ?

for _ in range(4):
    turtle.forward(100)
    turtle.left(90)

# Create a triangle
for _ in range(3):
    turtle.forward(100)
    turtle.left(120)

# Create a rectangle width: 100, height: 50
turtle.color("blue")
turtle.fillcolor("blue")
turtle.begin_fill()

for _ in range(2):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
turtle.end_fill()

screen.exitonclick()