import turtle
i = 0
turtle.begin_fill()
turtle.fillcolor('red')
turtle.pensize(10)
turtle.pencolor('green')
while i < 5:
    turtle.forward(200)
    turtle.left(72)
    i += 1
turtle.end_fill()
