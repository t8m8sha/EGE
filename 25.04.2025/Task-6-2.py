from turtle import *
m = 8
tracer(0)
lt(90)

rt(45)
for i in range(10):
    rt(45)
    fd(203*m)
    rt(45)
up()
bk(40*m)
rt(45)
down()
for i in range(5):
    fd(20*m)
    lt(90)
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(3,'red')
update()
done()
#nie robit