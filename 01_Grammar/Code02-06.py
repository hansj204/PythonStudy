import turtle

myTurtle = None

myTurtle = turtle.Turtle();
myTurtle.shape('turtle')

for i in range(0, 4) : 
    myTurtle.forward(200)
    myTurtle.right(90)

turtle.done()

exit()