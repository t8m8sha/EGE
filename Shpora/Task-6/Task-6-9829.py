from turtle import *
tracer(0)
lt(90)
screensize(10_000,10_000)
m = 50

rt(90)
for i in range(3):
    rt(45)
    fd(10*m)
    rt(45)
rt(315)
fd(10*m)
for i in range(2):
    rt(90)
    fd(10*m)
up()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*m,y*m)
        dot(5,'red')
update()
done()