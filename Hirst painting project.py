#Project Description: Hirst Painting Project 🎨
#Overview
#The Hirst Painting Project is a Python program that uses the Turtle graphics module to generate a dot-based artwork inspired by Damien Hirst's
#dot paintings. The program extracts colors from an image using the Colorgram library and then uses Turtle to randomly place dots in those colors on the screen.
#
#Project Features
#Extract Colors from an Image:
#
#Uses colorgram to extract 30 dominant colors from 'image.jpg'.
#Converts the extracted colors into RGB format.
#Randomized Dot Painting:
#
#The turtle moves across the canvas and randomly selects colors to create a grid of dots.
#Uses penup() to move without drawing lines.
#Each dot is 20 pixels in size, and the turtle moves 50 pixels apart to maintain spacing.
#Automated Grid Formation:
#
#The turtle follows a structured pattern to create rows of dots.
#After every 8 dots, it moves downwards to start a new row.
#Interactive Output:
#
#The Turtle screen remains open until the user clicks to close it.

import colorgram
import turtle as turtle_module
import random
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.penup()
tim.speed('fastest')
tim.hideturtle()
colors = colorgram.extract('image.jpg', 30)
print(colors)



rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)
    
print(rgb_colors)

color_list = [(252, 250, 247), (253, 247, 249), (237, 251, 245), (249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]

tim.dot(20, random.choice(color_list))

tim.setheading(255)
tim.forward(300)
tim.setheading(0)
number_of_dots = 88

for dot_count in range(0, number_of_dots):
    tim.dot(20, random.choice(color_list)) # The first parameter is the size
    tim.forward(50)
    
    if dot_count % 8 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick