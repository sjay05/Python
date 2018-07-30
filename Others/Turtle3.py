import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

bob = turtle.Turtle()
bob.color("red")
bob.pensize(1)

count = 0

while count <= 3:
    bob.forward(50)
    bob.right(120)
    count += 1

wn.exitonclick()
