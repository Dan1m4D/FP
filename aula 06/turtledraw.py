# Exercise 5 on "How to think like a computer scientist", ch. 11.
#def updown():
#    with open(, "r") as fin:
#        for line in fin:
#            if line == "UP":


import turtle

t = turtle.Turtle()

with open (updownxy.txt, "r") as fin:
    for line in fin:
        if line == "UP":
            t.up() 
        if line == "DOWM":
            t.down()
        fin.split("")
        
        

# Use t.up(), t.down() and t.goto(x, y)

# Put your code here
...

# wait
turtle.Screen().exitonclick()

