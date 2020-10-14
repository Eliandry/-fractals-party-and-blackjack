import turtle

axiom = "a"
axmTemp = ""
itr = 7  # итераций
dl = 5  # длина черты
turtle.hideturtle()
turtle.penup()
turtle.setpos(-300, -250)  # начальная позиция
turtle.pendown()
turtle.tracer(0)
turtle.pensize(2)

translate = {"a": "b-a-b",
             "b": "a+b+a"}

for k in range(itr):
    for ch in axiom:
        if ch in translate:
            axmTemp += translate[ch]
        else:
            axmTemp += ch
    axiom = axmTemp
    axmTemp = ""

for ch in axiom:
    if ch == "+":  # +
        turtle.right(60)
    elif ch == "-":  # -
        turtle.left(60)
    else:  # a b
        turtle.forward(dl)

turtle.update()
turtle.mainloop()
