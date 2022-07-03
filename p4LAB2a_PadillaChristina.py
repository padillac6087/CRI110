# Drawing a square and triangle using Turtle
#7/2/2022
#CTI-110
#P4Lab - Turtle Graphic
#Christina V Padilla

#Starting and ending with main to define the points of execution
def main():

#Bring in turtle and adding flare
    import turtle
    t = turtle.Turtle()
    t.pensize(4)
    t.pencolor('green')
    t.shape("turtle")
#first part was a square, then a triangle
#Was happy it turned into a house
    for x in range (4):
        t.forward(100)
        t.right(90)
    for y in range (3):
        t.forward(100)
        t.left(120)
main()
