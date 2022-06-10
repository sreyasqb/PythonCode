from pygame import *
root=display.set_mode((1000,500))
run=True
x=500
y=200
height=100
width=100
x1=200
y1=200
h1=50
w1=50
while run:
    for events in event.get():
        if events.type==QUIT:
            run=False
            break
    keys=key.get_pressed()
    if keys[K_RIGHT] and x<1000-width:
        x+=1

    if keys[K_LEFT] and x>0:
        x-=1

    if keys[K_UP] and y>0:
        y-=1

    if keys[K_DOWN] and y<500-height:
        y+=1

    if keys[K_d]:
        x1+=1
    if keys[K_a]:
        x1-=1
    root.fill((255,255,255))
    draw.rect(root,(0,255,0),(x,y,width,height))
    draw.rect(root,(255,0,0),(x1,y1,w1,h1))
    display.update()