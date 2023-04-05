import turtle

frogscreen = turtle.Screen()
frogscreen.bgcolor('black')
frogger = turtle.Turtle()
frogger.shape('triangle')
frogger.color('red')

frogger.penup()
size = 10
for i in range(125):
    frogger.stamp()
    frogger.pencolor('blue')
    size = size + 5
    frogger.forward(size)
    frogger.left(100)

turtle.color('white')
turtle.penup()
turtle.goto(-380,-200)
turtle.pendown()

turtle.write('Noah Stone', font=("Arial", 20, "normal"))

frogscreen.mainloop()
