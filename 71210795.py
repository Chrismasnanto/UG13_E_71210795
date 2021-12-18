import turtle

an = turtle.Screen()
a = turtle.Turtle()
a.shape("turtle")
a.color("black")
an.bgcolor("red")
a.speed(3)

stark1 = [[(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10),
           (-40, -20), (0, -20)],
          [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260),
           (40, 120), (0, 120)]]
stark2 = [[(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210),
           (-80, -230), (-64, -210), (0, -210)],
          [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40),
           (100, -46), (50, -40), (40, -30), (0, -30)]]
stark3 = [[(-60, -220), (-80, -240), (-110, -220), (-120, -250), (-90, -280), (-60, -260), (-30, -260), (-20, -250),
           (0, -250)],
          [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250), (110, -220), (80, -240), (60, -220),
           (0, -220)]]

turtle.hideturtle()
turtle.bgcolor('red')  # Dark Red
turtle.setup(500, 600)
turtle.title("I AM IRONMAN")
stark1Goto = (0, 120)
stark2Goto = (0, -30)
stark3Goto = (0, -220)
turtle.speed(3)


def logo(a, b):
    turtle.penup()
    turtle.goto(b)
    turtle.pendown()
    turtle.color('#fab104')  # Light Yellow
    turtle.begin_fill()

    for i in range(len(a[0])):
        x, y = a[0][i]
        turtle.goto(x, y)

    for i in range(len(a[1])):
        x, y = a[1][i]
        turtle.goto(x, y)
    turtle.end_fill()
logo(stark1, stark1Goto)
logo(stark2, stark2Goto)
logo(stark3, stark3Goto)
turtle.hideturtle()
 
#huruf D
a.penup()
a.goto(-230, -300)
a.pendown()
a.pensize(25)
a.circle(50, 180)
a.left(90)
a.forward(100)
a.right(180)

# huruf I
a.penup() 
a.goto(-130, -300)
a.down()
a.left(100)
a.pensize(25)
a.pendown()
a.setheading(90)
a.forward(100)
a.setheading(0)
a.penup()

# huruf M
a.goto(-80, -200)
a.pendown()
a.pensize(25)
a.right(90)
a.forward(90)
a.backward(90)
a.left(45)
a.forward(90)
a.left(95)
a.forward(90)
a.right(140)
a.forward(100)
a.penup()

# huruf A
a.goto(130, -190)
a.pendown()
a.pensize(25)
a.right(25)
a.forward(110)
a.backward(110)
a.left(45)
a.forward(110)
a.backward(45)
a.right(100)
a.forward(35)
a.penup()

# huruf S
a.goto(240, -290)
a.pendown()
a.pensize(25)
a.pendown()
a.forward(30)
a.backward(30)
a.circle(-25, -170)
a.circle(25, -235)
a.penup()

turtle.done()
