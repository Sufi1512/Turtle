import turtle
col=('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo',  'Violet', )
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('Black')
t.speed(60)
for i in range (110):
    t.color(col[i%7])
    t.forward(i*7)
    t.left(155)
    t.width(2)

s.exitonclick()
