from pygame import *
root=display.set_mode((1000,600))
run=True
x=100
y=200
while run:
    for events in event.get():
        if events.type==QUIT:
            run=False
    root.fill((255,255,255))
    draw.rect(root,(255,0,0),(x,y,40,40))
    x+=0.01
    display.update()