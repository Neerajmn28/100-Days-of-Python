import turtle
import random


tim = turtle.Turtle()

from turtle import Turtle, Screen # Importing the class directly

# Another way is importing everything
from turtle import *

# Aliasing the library
import turtle as t



colors = ['DarkOrchid','IndianRed','DeepSkyBlue','wheat','LightSeaGreen','CornflowerBlue']
directions = [0,90,180,270]
turtle.colormode(255)

def random_color():
    r = random.randint(0,255) 
    g = random.randint(0,255)
    b = random.randint(0,255) 
    random_color = (r,g,b)
    return random_color

for _ in range(200):
    tim.forward(30)
    tim.color(random_color())
    tim.setheading(random.choice(directions))
    tim.pensize(15)

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
    
num_sides = 5   
def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
        
        


        
for shape_side_n in range(3,11):
    turtle.color()
    draw_shape(shape_side_n)
    

 
        
directions = [0,90,100,270]
tim.pensize(15)
tim.speed("fastest")






