# Drawing a snowflack
#7/2/2022)
#CTI-110
#P4Lab - Turtle Graphic
#Christina V Padilla

#Starting and ending with main to define the points of execution
def main():

#Bring in turtle and adding flare
    import turtle
    t = turtle.Turtle()
    t.pensize(4)
    t.pencolor('purple')
    t.shape("turtle")
#Moving to a point to make your snowflake centered
    t.penup()
    t.forward(90)
    t.left(45)
    t.pendown()
#Creating a branch to make each limb of the snowflake
    def branch():
        for i in range(3):
            for i in range(3):
                t.forward(30)
                t.backward(30)
                t.right(45)
            t.left(90)
            t.backward(30)
            t.left(45)
        t.right(90) 
        t.forward(90)
#Executing the branch        
    for i in range(8):
        branch()
        t.left(45)

main()
