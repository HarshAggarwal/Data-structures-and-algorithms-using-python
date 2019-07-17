import turtle as t
def sier(n,length):
    if (n==0):
        return
    for i in range(3):
        sier(n-1, length/2)
        t.fd(length)
        t.rt(120)
 

from numpy import *
import turtle
 
def Left(turn, point, fwd, angle, turt):
	turt.left(angle)
	return [turn, point, fwd, angle, turt]
def Right(turn, point, fwd, angle, turt):
	turt.right(angle)
	return [turn, point, fwd, angle, turt]
def Forward(turn, point, fwd, angle, turt):
	turt.forward(fwd)
	return [turn, point, fwd, angle, turt]
 


def DrawSierpinskiTriangle(level, ss=400):
	# typical values
	turn = 0		# initial turn (0 to start horizontally)
	angle=60.0 		# in degrees
 
	# Initialize the turtle
	turtle.hideturtle()
	turtle.screensize(ss,ss)
	turtle.penup()
	turtle.degrees()
 
	fwd0         = float(ss)
	point=array([-fwd0/2.0, -fwd0/2.0])
 
 
	decode    = {'-':Left, '+':Right, 'X':Forward, 'H':Forward}
	axiom     = 'H--X--X'
 
	turtle.goto(point[0], point[1])
	turtle.pendown()
	turtle.hideturtle()
	turt=turtle.getpen()
	startposition=turt.clone()
 
	fwd       = fwd0/(2.0**level)
	path      = axiom
	for i in range(0,level):
		path=path.replace('X','XX')
		path=path.replace('H','H--X++H++X--H')

	for i in path:
		[turn, point, fwd, angle, turt]=decode[i](turn, point, fwd, angle, turt)

 
DrawSierpinskiTriangle(5)