import turtle

main_screen = turtle.Screen()
main_screen.bgcolor("skyblue")
main_screen.title("Drawing Game")

arrow = turtle.Turtle()

def Forward():
    arrow.forward(10)

def AngleRight():
    arrow.right(10)

def AngleLeft():
    arrow.left(10)

def Clear():
    arrow.clear()

def ReturnHome():
    arrow.home()

def PenUp():
    arrow.penup()

def PenDown():
    arrow.pendown()

main_screen.listen()
main_screen.onkey(fun=Forward,key="space")
main_screen.onkey(fun=AngleRight,key="Right")
main_screen.onkey(fun=AngleLeft,key="Left")
main_screen.onkey(fun=Clear,key="c")
main_screen.onkey(fun=ReturnHome,key="r")
main_screen.onkey(fun=PenUp,key="o")
main_screen.onkey(fun=PenDown,key="p")

turtle.done()

