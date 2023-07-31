import turtle
import colorsys

arrow = turtle.Turtle()

turtle_screen = turtle.Screen().bgcolor('black')

arrow.speed(0)
arrow.hideturtle()

color_palette = 200
a = 0

for i in range(400):
    color = colorsys.hsv_to_rgb(a, 1, 0.8)
    a = a + 1/color_palette
    arrow.color(color)
    arrow.right(1)
    arrow.fd(1)
    for j in range(5):
        arrow.left(60)
        arrow.forward(100)