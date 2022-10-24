"""
draws 'Sierpinski squares' recursively
"""

from turtle import Turtle, Screen
turtle = Turtle()
screen = Screen()


def draw_square(starting_point, side_length, color=None, turtle=None):
    assert isinstance(turtle, Turtle)
    turtle.speed('fastest')
    turtle.up()
    turtle.goto(*starting_point)
    turtle.setheading(0)
    turtle.down()

    turtle.fillcolor(color or 'yellow')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(side_length)
        turtle.right(90)
    else: turtle.end_fill()
    return turtle


def draw_four_squares(starting_point, side_length, color=None, turtle=None):
    assert isinstance(turtle, Turtle)
    gap = side_length / 25
    if side_length < 10: return
    assert side_length > gap*4

    color = color or 'green'
    draw_square(starting_point, side_length, color=color, turtle=turtle)

    inner_side_length = (side_length-3*gap)/2
    offset = 2*gap + inner_side_length

    x,y = starting_point
    inner_squares_coordinates = [(x+gap, y-gap), (x+offset, y-gap), (x+gap, y-offset), (x+offset, y-offset)]

    colours = ('red', 'green', 'blue', 'yellow')
    for i,coordinates in enumerate(inner_squares_coordinates):
        draw_four_squares(coordinates, inner_side_length, color=colours[i], turtle=turtle)




startingpoint = (-200,250)
sidelength = 300

draw_four_squares(starting_point=startingpoint, side_length=sidelength, turtle=turtle)
screen.exitonclick()
