import turtle

turtle.title("My Turtle Game")
turtle.bgcolor("blue")
turtle.setup(600,600)
screen = turtle.Screen()
bob = turtle.Turtle()
bob.shape("turtle")






def star(length, red):
  bob.fillcolor(red)
  bob.begin_fill()
  x=0
  while x <15:
    bob.forward(int(length))
    bob.right(144)
    x += 1
  bob.end_fill()