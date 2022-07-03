# Drawing my C and P from my name
#7/2/2022
#CTI-110
#P4Lab - Turtle Graphics
#Christina V Padilla

#Starting and ending with main to define the points of execution
def main():

#Bring in turtle and adding flare
    import turtle
    t = turtle.Turtle()
    t.pensize(4)
    t.pencolor('green')
    t.shape("turtle")
#Creating a C and P making sure they are the same size in appearance
    for c in range (1):
        t.right(180)
        t.circle(50,180)

    t.penup()
    t.forward(50)
    t.pendown()
    
    for p in range (1):
        t.left(90)
        t.forward(50)
        t.right(90)
        t.circle(25,180)
        t.left(90)
        t.forward(50)

main()
