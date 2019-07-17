import turtle

def ftree(branch_len , t):
	if(branch_len > 5):
		t.forward(branch_len)
		t.right(20)
		ftree(branch_len-15 , t)
		t.left(40)
		ftree(branch_len-15 , t)
		t.right(20)
		t.backward(branch_len)

def main():
	t = turtle.Turtle()
	my_win = turtle.Screen()
	t.left(90)
	t.up()
	t.backward(100)
	t.down()
	t.color('green')
	ftree(75,t)
	my_win.exitonclick()

main()