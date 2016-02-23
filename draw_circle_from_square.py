import turtle

def draw_circle():
    window = turtle.Screen()
    window.bgcolor("pink")
    draw_circle_from_square("square", "red", 15)
    window.exitonclick()

def create_turtle(shape, color, speed):
    newTurtle = turtle.Turtle()
    newTurtle.shape(shape)
    newTurtle.color(color)
    newTurtle.speed(speed)
    return newTurtle

def draw_circle_from_square(shape, color, speed):
    squareTurtle = create_turtle(shape, color, speed)
    
    angle = 2

    while angle < 360:
        for i in range(0,4):
            squareTurtle.forward(100)
            squareTurtle.right(90)
        squareTurtle.right(angle)
        angle += 2

draw_circle()

