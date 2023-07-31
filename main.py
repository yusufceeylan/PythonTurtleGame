import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("white")
turtle_screen.title("Turtle Game")

turtleDrawer = turtle.Turtle()
turtleDrawer.color("red")
turtleDrawer.shape("turtle")

def right():
    turtleDrawer.forward(20)
def left():
    turtleDrawer.forward(20)
def up():
    turtleDrawer.left(90)
    turtleDrawer.forward(20)
def down():
    turtleDrawer.right(90)
    turtleDrawer.forward(20)

turtle.listen()
turtle.onkey(turtleDrawer.clear,"d")
turtle.onkey(right,"Right")
turtle.onkey(left,"Left")
turtle.onkey(up,"Up")
turtle.onkey(down,"Down")

turtle.done()


