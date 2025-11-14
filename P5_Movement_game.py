# Section 1 - Helper functions (DON'T CHANGE!!)
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


# Section 2: Setup
s1 = create_sprite("Kirby",0,-150) # main character sprite

# food sprites

s2 = create_sprite("Salad",random.randint(-350, 350),600) 
s3 = create_sprite("Burger1",random.randint(-350, 350),385)
s4 = create_sprite("ChickenFood1",random.randint(-350, 350),500)

s5 = create_sprite("Line",0,-325)


set_background("Cool_gradient1")


Lives = 3 




# Section 3: Controls
def move_up():
	s1.setheading(90)
	s1.forward(5)
        
def move_down():
	s1.setheading(270)
	s1.forward(5)
    
def move_left():
	s1.setheading(180)
	s1.forward(5)
    
def move_right():    
	s1.setheading(0)
	s1.forward(5)


# Bind arrow keys to the movement functions for sprite s1
window.onkey(move_up, "Up")
window.onkey(move_down, "Down")
window.onkey(move_left, "Left")
window.onkey(move_right, "Right")



# Section 4: Game Loop
window.listen()





timer = 0
while True:
	time.sleep(0.1)
	timer += 1

	# TODO - code for automatic actions
	s2.setheading(270)
	s2.forward(5)

	s3.setheading(270)
	s3.forward(5)

	s4.setheading(270)
	s4.forward(5)







	if get_distance(s1, s2) < 50:
		
		s2.goto (random.randint(-350, 350),400)



	if get_distance(s1, s3) < 50:



		s3.goto (random.randint(-350, 350),500)



	if get_distance(s1, s4) < 50:
		s4.goto (random.randint(-350, 350),500)
		


	if s2.ycor() < -290:
		Lives -= 1
		s2.goto (random.randint(-350, 350),600)
		
	elif s3.ycor() < -290:
		Lives -= 1	
		s3.goto (random.randint(-350, 350),500)

	elif s4.ycor() < -290:
		Lives -= 1
		s4.goto (random.randint(-350, 350),500)



	window.update() 




	# optional: end the game when Lives reaches 0
	if Lives <= 0:
		print("Game Over!")
		break 































