from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
    
def move_backwards():
    tim.backward(10)
    
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    
def clear():
    tim.clear() # delete the turtle's drawings from the screen
    tim.penup()
    tim.home() # Move the turtle to the orgin
    tim.pendown()
    
screen.listen() # Set focus on TurtleScreen (in order to collect key - Events)
screen.onkey(move_forwards, 'w')
screen.onkey(move_backwards, 's' )
screen.onkey(turn_left,'a')
screen.onkey(turn_right,'d')


screen.exitonclick()