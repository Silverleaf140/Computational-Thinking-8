# Section 1 - Helper functions (DON'T CHANGE THIS!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
 
def set_image(sprite, image_filename):
    image_file = f"./Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite.shape(image_file)
 
def create_sprite(image_filename, x=0, y=0):
    sprite = turtle.Turtle()
    set_image(sprite, image_filename) 
    sprite.penup()
    sprite.goto(x,y)
    window.update()
    return sprite
 
def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)
 
def draw_rectangle( color="black",x=0,y=0, width=100, height=100,):
	sprite = turtle.Turtle()
	sprite.speed(0)
	sprite.pencolor(color)
	sprite.color(color)
	sprite.penup()
	sprite.goto(x - (width*0.5), y + (height*0.5))
	sprite.pendown()
	sprite.begin_fill()
	for i in range(2):
		sprite.forward(width)
		sprite.right(90)
		sprite.forward(height)
		sprite.right(90)
	sprite.end_fill()
	sprite.hideturtle()
 
 
window = turtle.Screen()
window.tracer(0)





import turtle
t = turtle.Turtle()

#

t.speed(10)
t.goto(-180,0)
turtle.Screen() .bgcolor ("black")
t.color("blue")

#art code 

colors = ["red", "orangered", "tomato", "dark orange", "gold", "yellow", "lemonchiffon", "light yellow"]

message1 = create_sprite ("alien",-45,35)
message1.color("red") 
message1.write("CT8",font = ("Arial", 30, "normal", "bold"))
message1.hideturtle()


for i in range(160):
    t.color( colors[i % 8 ] )
    t.forward(350)
    t.left(500 + 1)
	
t.penup

window.update()

turtle.exitonclick()

















