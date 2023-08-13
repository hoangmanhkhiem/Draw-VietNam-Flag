import turtle
wn = turtle.Screen()
wn.bgcolor("red")
screen_width = 750;
screen_height = 500;
star_length = 200;

wn.setup(width = screen_width, height = screen_height)
wn.title("Tôi Yêu Việt Nam")

vin = turtle.Turtle()
vin.color("red")

vin.setx((screen_width - star_length)/2 - screen_width/2)
vin.sety(star_length/4)
vin.color("yellow")
vin.shape("turtle")
vin.pensize(3)
vin.speed(2)

for counter in range(5):
    vin.forward(star_length)
    vin.right(144)
vin.goto((screen_width - star_length)/2 - screen_width/2,star_length/4)
vin.setheading(0)
vin.pendown()
vin.begin_fill()
vin.color("yellow")
for turn in range(0,5) :
    vin.forward(star_length)
    vin.right(144)
    vin.forward(star_length)
    vin.right(144)
vin.end_fill()
vin.penup()
vin.shape("blank")
wn.exitonclick()
