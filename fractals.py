import turtle

turtle.hideturtle()
turtle.tracer(0)
turtle.penup()
turtle.setposition(-400,500)
turtle.pendown()
turtle.pensize(2)
turtle.setup(1920,1080)

axiom = "F+F+F+F"
tempAx = ''
itr = 4
trans = {"+": "+", "-": "-", "F": "F+F-F-F+F"}
for k in range(itr):
    for i in axiom:
        tempAx = tempAx + trans[i]
    axiom = tempAx
    tempAx = ""

for ch in axiom:
    if ch == "+":
        turtle.right(90)

    elif ch == "-":
        turtle.left(90)
    else:
        turtle.forward(10)
turtle.update()
turtle.mainloop()
