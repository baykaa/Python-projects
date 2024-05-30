import turtle
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("clock")

# alex = turtle.Turtle()       # Create alex
# alex.color("Red")
# alex.pensize(3)

# for i in range(4):
#     alex.forward(100)             # Make alex draw a square
#     alex.left(90)

# love = turtle.Turtle()
# love.color("Red")
# love.pensize(4)
# love.speed(10)

# love.left(45)
# love.forward(100)
# love.left(90)
# love.forward(50)
# love.left(90)
# love.forward(50)
# love.right(90)
# love.forward(50)
# love.left(90)
# love.forward(50)
# love.left(90)
# love.forward(100)


# finger = turtle.Turtle()
# finger.pensize(3)
# finger.forward(100)


# tria = turtle.Turtle()
# tria.color("Blue")
# tria.pensize(4)
# tria.shape("turtle")
# tria.speed(5)

# for c in ["yellow", "red", "purple", "blue"]:
#     tria.color(c)
#     tria.forward(50)
#     tria.left(90)

# tess = turtle.Turtle()
# tess.shape("turtle")
# tess.color("blue")

# tess.penup()                # This is new
# size = 20
# for i in range(30):
#    tess.stamp()             # Leave an impression on the canvas
#    size = size + 3          # Increase the size on every iteration
#    tess.forward(size)       # Move tess along
#    tess.right(24)           #  ...  and turn her

# EXERCISE - 6
# hex = turtle.Turtle()
# for i in range(6):
#     hex.forward(100)
#     hex.right(60)


# oct = turtle.Turtle()
# oct.color("green")
# for j in range(8):
#     oct.forward(100)
#     oct.right(45)

# EXERCISE - 7
# oldman = turtle.Turtle()
# oldman.color("brown")
# steps = [160, -43, 270, -97, -43, 200, -940, 17, -86]
# for step in steps:
#     oldman.forward(100)
#     oldman.left(step)

#EXERCISE - 9
# n = 15
# interior_angle = 180 - (180 * (n - 2)) / n

# print(interior_angle)
# drawing = turtle.Turtle()
# for angle in range(n):
#     drawing.forward(40)
#     drawing.left(interior_angle)



#EXERCISE - 10 

# star = turtle.Turtle()
# star.color("Yellow")
# star.pensize(3)

# for i in range(5):
#     star.forward(100)
#     star.right(144)

# EXERCISE - 11

# import turtle
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# tess = turtle.Turtle()
# tess.shape("turtle")
# tess.color("blue")

# tess.penup()                # This is new
# size = 20
# for i in range(30):
#    tess.stamp()             # Leave an impression on the canvas
#    size = size + 3          # Increase the size on every iteration
#    tess.forward(size)       # Move tess along
#    tess.right(24)           #  ...  and turn her
# wn.mainloop()

clock = turtle.Turtle()
clock.color("blue")
clock.pensize(3)

clock.penup()
clock.shape("turtle")

def forward_stamp():
    clock.forward(80)
    clock.pendown()
    clock.forward(10)
    clock.penup()
    clock.forward(20)
    clock.stamp()

# Go back function
def go_backward():
    clock.right(180)
    clock.forward(110)
    clock.left(150)

for i in range(12):
    forward_stamp()
    go_backward()

wn.mainloop()