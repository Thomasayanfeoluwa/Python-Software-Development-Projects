# import colorgram
#
# rgb_colors = []
#
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
# 	r = color.rgb.r
# 	g = color.rgb.g
# 	b = color.rgb.b
# 	new_color = (r, g, b)
# 	rgb_colors.append(new_color)
#
# print(rgb_colors)
"You use the code above to get the color_list which you'll use to get the real work done."

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(79, 254, 153), (197, 254, 225), (173, 146, 121), (0, 0, 180), (254, 37, 187), (149, 56, 251), (157, 106, 56), (218, 254, 102), (254, 147, 201), (253, 0, 251), (0, 218, 191), (255, 147, 147), (1, 86, 175), (252, 0, 0), (254, 69, 69), (35, 35, 254), (252, 229, 246), (211, 208, 243), (139, 153, 212), (186, 159, 247), (238, 106, 204), (0, 212, 217), (251, 138, 0), (136, 0, 254), (147, 230, 235)]
tim.setheading(255)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots +1):
	tim.dot(20, random.choice(color_list))
	tim.forward(50)

	if dot_count % 10 == 0:
		tim.setheading(90)
		tim.forward(50)
		tim.setheading(180)
		tim.forward(500)
		tim.setheading(0)

