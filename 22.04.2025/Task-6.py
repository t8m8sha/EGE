from turtle import *
tracer (0)
m = 8
lt(90)
for i in range(7):
    fd(9*m)
    rt(90)
    fd(16*m)
    rt(90)
up()
fd(3*m)
rt(90)
fd(4*m)
lt(90)
down()
for i in range(4):
    fd(7*m)
    rt(90)
    fd(13*m)
    rt(90)
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(3,'red')
done()
