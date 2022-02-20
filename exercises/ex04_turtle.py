"""A drawing of a house complete with many windows using the Turtle.

For Point 7 'Break up complex functions' the function 'roof_outline' in lines 118-155 is broken into triangle_top 
in lines 93-115 and line_between in lines 158-166. For Point 8 'Try something fun!' the randomized windows created
in lines 43-65 make use of random integers to randomize size, position, and color.
"""

__author__ = "730518701"

from random import randint
from turtle import Turtle, colormode, done
colormode(255)

SQUARE_ROOT_OF_2: float = (2 ** (1 / 2))


def main() -> None:
    """The start of a great big house scene.
    
    The length and height of the house are first defined, and starting positions are determined to center the house.
    The main_house shape is created first, then the roof, then the many windows are added last.
    """
    house_length: float = 500
    house_height: float = 250
    start_x: float = - (house_length / 2)
    start_y: float = house_height / 2
    
    main_house: Turtle = Turtle()
    roof: Turtle = Turtle()
    windows: Turtle = Turtle()
    
    # The person who lives in the main part of the house is of great taste, so they are a Carolina fan and the main house is colored accordingly.
    main_house.pencolor(0, 0, 0)
    main_house.fillcolor(102, 153, 194)
    short_rectangle(main_house, start_x, start_y, house_length, house_height / house_length)
    
    # The color of this outline of the roof and the inside triangle is Duke Blue, because a Duke fan haunts the attic. It is 20 units thick.
    roof.pencolor(0, 48, 135)
    roof.fillcolor(0, 48, 135)
    roof_thickness: float = 20
    roof_outline(roof, start_x, start_y, house_length, roof_thickness)
    
    # This loop draws randomly sized windows across the length of the house, spaced out by 50 units plus a random integer.
    # They are also randomly colored, therefore the Carolina fan has good taste in colleges but odd taste in windows.
    i: int = 0
    approximate_window_spacing: int = 50
    while i < (house_length // approximate_window_spacing):
        # First, the dimensions, position, and spacing are decided randomly. The position is a random number of window
        # lengths away from the roof, but it will stay within the house.
        window_length: int = randint(10, 20)
        window_height_position: float = start_y - (randint(1, int(house_height // window_length - 1)) * window_length)
        window_space: float = (start_x + window_length + i * approximate_window_spacing)
        window_proportion: float = (randint(10, 20) / 10)

        # Then, the windows are given random colors to be filled with.
        window_red: int = randint(0, 255)
        window_green: int = randint(0, 255)
        window_blue: int = randint(0, 255)
        windows.fillcolor(window_red, window_green, window_blue)

        # Finally, the windows are drawn with a function call using our randomly generated argumentsand the index is increased by 1.
        windows.begin_fill()
        vertical_rectangle(windows, window_space, window_height_position, window_length, window_proportion)
        windows.end_fill()
        i += 1

    done()


def vertical_rectangle(rectangle_turtle: Turtle, corner_x: float, corner_y: float, width: int, length_ratio: float) -> None:
    """Draws a filled rectangle with an inputted width and a length that is length_ratio times the width.
    
    The long side is vertically oriented. Can be used for windows. corner_x and corner_y are located at the top left corner.
    """
    rectangle_turtle.ht()
    rectangle_turtle.penup()
    rectangle_turtle.goto(corner_x, corner_y)
    rectangle_turtle.setheading(0.0)
    rectangle_turtle.pendown()
    
    i: int = 0
    length: float = width * length_ratio

    while i < 4:
        if i % 2 == 0:
            rectangle_turtle.forward(width)
        else:
            rectangle_turtle.forward(length)
        rectangle_turtle.right(90)
        i += 1


def triangle_top(triangle_turtle: Turtle, corner_x: float, corner_y: float, hypotenuse_length: float) -> None:
    """Draws a 1:1:root(2) right triangle with an invisible hypotenuse on the bottom of inputted length.
    
    Assists roof function. corner_x and corner_y are located at the bottom left corner.
    """
    triangle_turtle.penup()
    triangle_turtle.goto(corner_x, corner_y)
    triangle_turtle.setheading(0.0)

    i: int = 0
    # The length of this special right triangle's legs are determined by Pythogorean Theorem
    triangle_leg_length: float = (hypotenuse_length / SQUARE_ROOT_OF_2)

    while i < 3:
        if i == 0:
            # This first side of the triangle is intentionally invisible.
            triangle_turtle.forward(hypotenuse_length)
            triangle_turtle.left(135)
        else:
            triangle_turtle.pendown()
            triangle_turtle.forward(triangle_leg_length)
            triangle_turtle.left(90)
        i += 1


def roof_outline(roofing_turtle: Turtle, inside_x: float, inside_y: float, inside_length: float, thickness: float) -> None:
    """Using the triangle_top function, draws a roof shape for the top of the house.
   
    inside_x and inside_y give the starting point that is the left bottom corner of the inner triangle.
    The length of the inside triangle is inputted as well as thickness. 
    The inside of the inner triangle is filled as well to give color to the roof.
    However, the inside of the roof itself is not colored in.
    """
    roofing_turtle.ht()

    # This first function call draws the inside triangle with no bottom. This triangle is filled with Duke blue (color defined in main()) because of the Duke fan in the attic.
    roofing_turtle.begin_fill()
    triangle_top(roofing_turtle, inside_x, inside_y, inside_length)
    roofing_turtle.end_fill()
    
    # The roofing turtle then lifts up and gets into position for the second, bigger triangle above
    roofing_turtle.penup()
    roofing_turtle.right(180)
    roofing_turtle.forward(thickness)

    # It is necessary to retrieve the new coordinate of the turtle here in order to call the triangle function again
    # and draw a bigger triangle in the right position.
    corner_big_triangle_x: float = roofing_turtle.xcor()
    corner_big_triangle_y: float = roofing_turtle.ycor()

    # Pen-and-paper calculations of the shape of the roof using right triangles reveal that with this type of roof shape,
    # the length of the hypotenuse of the larger triangle is proportional to the hypotenuse of the inner triangle plus the thickness of the 
    # roof multiplied by the square root of 2, due to the Pythagorean theorem. Drawing right triangles with the thickness as the hypotenuse
    # of two different right triangles reveals this relationship.
    big_length: float = (inside_length + (thickness * SQUARE_ROOT_OF_2))

    # This function call draws the larger triangle on top of the smaller one.
    triangle_top(roofing_turtle, corner_big_triangle_x, corner_big_triangle_y, big_length)
    
    # These two line_between function calls will complete the roof shape by connecting the tips of each triangle.
    line_between(roofing_turtle, corner_big_triangle_x, corner_big_triangle_y, inside_x, inside_y)
    # This second function call must change the x of the starting position by each triangle's length in order to connect the two other tips.
    line_between(roofing_turtle, corner_big_triangle_x + big_length, corner_big_triangle_y, inside_x + inside_length, inside_y)


def line_between(line_turtle: Turtle, start_x: float, start_y: float, end_x: float, end_y: float) -> None:
    """Draws a straight line between the points (start_x, start_y) and (end_x, end_y).
    
    Assists roof function and could help many others if needed.
    """
    line_turtle.penup()
    line_turtle.goto(start_x, start_y)
    line_turtle.pendown()
    line_turtle.goto(end_x, end_y)


def short_rectangle(short_rect_turtle: Turtle, corner_x: float, corner_y: float, width: float, length_ratio: float) -> None:
    """Draws a rectangle similarly to vertical_rectangle.
    
    Starting at the top left corner (at (corner_x, corner_y)), with the top side missing.
    This function also has an inputted width and ratio of width to length. 
    This will serve as the overall shape of the house.
    """
    short_rect_turtle.ht()
    short_rect_turtle.penup()
    short_rect_turtle.setpos(corner_x, corner_y)
    short_rect_turtle.setheading(270)
    short_rect_turtle.pendown()
    short_rect_turtle.begin_fill()

    i: int = 0
    length: float = width * length_ratio

    # This loop draws only 3 sides of a rectangle starting with the left side and going down.
    while i < 3:
        if i % 2 == 0:
            short_rect_turtle.forward(length)
            short_rect_turtle.left(90)
        else:
            short_rect_turtle.forward(width)
            short_rect_turtle.left(90)
        i += 1

    short_rect_turtle.end_fill()

    
if __name__ == "__main__":
    main()