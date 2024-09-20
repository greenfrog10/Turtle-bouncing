def execute_script():
    import turtle
    import random
    run = True
    gravity = -0.0001
    x = -0.01
    velocity = 0
    width = 500
    height = 500
    window = turtle.Screen()
    window.setup(width, height)
    window.title("Bouncing Simulation")
    window.bgcolor("light green")
    window.tracer(0)
    ball = turtle.Turtle()
    ball.penup()
    ball.shape("turtle")
    ball.color("red")
    ball.shapesize(3)
    i = 0
    while run:
        ball.setheading(90 + i)
        i += 0.1
        ball.sety(ball.ycor() + velocity)
        ball.setx(ball.xcor() - x)
        if ball.xcor() > 220:
            x = 0.01
        if ball.xcor() < -220:
            x = -0.01
        velocity += gravity
        if ball.ycor() < -220:
            velocity = -velocity
        if ball.ycor() > 220:
            velocity = velocity 
        window.update()
execute_script()
