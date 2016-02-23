import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("pink")

    draw_square("square","purple",2)

    draw_circle("circle", "blue", 2)

    draw_triangle("triangle", "red", 3)
    
    window.exitonclick()

def create_turtle(shape, color, speed):
    newTurtle = turtle.Turtle()
    newTurtle.shape(shape)
    newTurtle.color(color)
    newTurtle.speed(speed)
    return newTurtle

def draw_square(shape, color, speed):
    squareTurtle = create_turtle(shape, color, speed)
    
    for i in range(0,4):
        squareTurtle.forward(100)
        squareTurtle.right(90)

def draw_circle(shape, color, speed):
    circleTurtle = create_turtle("circle", "blue", 2)
    
    circleTurtle.circle(100)

def draw_triangle(shape, color, speed):
    triTurtle = create_turtle("triangle", "red", 3)
    
    for i in range(0,3):
        triTurtle.backward(130)
        triTurtle.left(120)

draw_shapes()

