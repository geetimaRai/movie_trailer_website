import turtle

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("pink")
    draw_flower_from_rhombus("turtle", "red", 20)
    window.exitonclick()

def create_turtle(shape, color, speed):
    newTurtle = turtle.Turtle()
    newTurtle.shape(shape)
    newTurtle.color(color)
    newTurtle.speed(speed)
    return newTurtle

def draw_flower_from_rhombus(shape, color, speed):
    starTurtle = create_turtle(shape, color, speed)
    
    angle = 5
    count = angle
    turn_angle = 150
    
    while count <= 360:
        for i in range(0,4):
            starTurtle.forward(50)
            if turn_angle == 150:
                turn_angle = 30
                starTurtle.right(turn_angle)
            else:
                turn_angle = 150
                starTurtle.right(turn_angle)

        starTurtle.right(angle)
        count += angle
    starTurtle.right(90)
    starTurtle.forward(250)

draw_flower()

