from turtle import*


bgcolor("yellow")
width(20)
penup()
goto(100, 100)
pendown()
fillcolor("white")
begin_fill()
setheading(90)
circle(100,180)
fd(30)
lt(-110)
fd(30)
circle(25,180)
fd(20)
setheading(85)
circle(140,-60)
lt(-65)
circle(250,13)
lt(-70)
fd(15)
lt(90)
fd(52)
setheading(-28)
circle(198,54)
setheading(0)
fd(52)
lt(90)
fd(15)
lt(-75)
circle(250,13)
lt(-65)
circle(140,-60)
setheading(5)
fd(30)
circle(25,180)
fd(30)
lt(-65)
fd(30)
end_fill()
if __name__ == '__main__':
    screensize(800, 600)
    pensize(3)
    speed(9)
    turtles() 
    write('     by Sufiyan Khan', font=("Bradley Hand ITC", 30, "bold" , ))
    mainloop()
exitonclick()



