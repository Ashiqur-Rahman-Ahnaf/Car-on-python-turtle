import turtle

def draw_body(t):
    t.penup()
    t.goto(-100, -50)
    t.pendown()
    t.color("blue")
    t.begin_fill()
    t.forward(180)
    t.left(0)
    t.circle(30.3,180)
    t.forward(180)
    t.left(0)
    t.circle(30.3,180)
    t.end_fill()

def draw_roof(t):
    t.penup()
    t.goto(-65, 0)
    t.pendown()
    t.color("blue")
    t.begin_fill()
    t.setheading(45)
    t.forward(70)
    t.setheading(0)
    t.forward(100)
    t.setheading(-90)
    t.forward(70)
    t.setheading(180)
    t.forward(150)
    t.end_fill()

def draw_windows(t):
    t.penup()
    t.goto(-45, 10)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.right(135)
    t.forward(50)
    t.right(45)
    t.forward(30)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(65)
    t.end_fill()
    
def draw_window(t):
    t.penup()
    t.goto(25, 5)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.right(95)
    t.forward(40)
    t.right(85)
    t.forward(50)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(55)
    t.end_fill()

def draw_wheels(t):
    t.penup()
    t.goto(-60,-20)
    t.pendown()
    t.color("white","black")
    t.begin_fill()
    t.circle(25)
    t.end_fill()

    t.penup()
    t.goto(60, -20)
    t.pendown()
    t.color("white","black")
    t.begin_fill()
    t.circle(25)
    t.end_fill()

def draw_headlights(t):
    t.penup()
    t.goto(95, -30)
    t.pendown()
    t.dot(15,"yellow")
    t.penup()
    t.goto(-105, -2)
    t.pendown()
    t.dot(20,"red")

def draw_car():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Car Drawing")
    car = turtle.Turtle()
    car.speed(1)
    car.speed(5)

    draw_body(car)
    draw_roof(car)
    draw_windows(car)
    draw_window(car)
    draw_wheels(car)
    draw_headlights(car)

    car.hideturtle()
    turtle.done()
draw_car()