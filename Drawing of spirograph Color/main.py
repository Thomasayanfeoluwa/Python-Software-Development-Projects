from turtle import Turtle, Screen
tim = Turtle()
tim.shape("turtle")
tim.color("green", "blue")
tim.forward(90)
tim.right(90)
tim.forward(90)
tim.right(90)
tim.forward(90)
tim.right(90)
tim.forward(90)

for _ in range(4):
	tim.shape("turtle")
	tim.color("green", "blue")
	tim.forward(90)
	tim.right(90)


screen = Screen()
screen.exitonclick()


import turtle as t

tim = t.Turtle()

for _ in range(15):
	tim.forward(10)
	tim.penup()
	tim.forward(10)
	tim.pendown()


screen = Screen()
screen.exitonclick()



import turtle as t
import random

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", " DeepSkyBlue" "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
	angle = 360 / num_sides
	for _ in range(num_sides):
		tim.forward(100)
		tim.right(angle)

for shape_side_n in range(3, 11):
	tim.color(random.choice(colours))
	draw_shape(shape_side_n)


























