from turtle import *
tracer(0)
m = 20
lt(90)
for i in range(3):
    fd(7*m)
    rt(90)
    fd(12*m)
    rt(90)
up()
fd(4*m)
rt(90)
fd(6*m)
lt(90)
down()
for i in range(4):
    fd(83*m)
    rt(90)
    fd(77*m)
    rt(90)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * m, y * m)
        dot(3, 'red')
update()
done()
#otvet: 6628