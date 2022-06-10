from pygame import *
root=display.set_mode((1300,800))
run=1
isjump=False
g=0.4
dt=0.01
x=0
y=0
image=image.load("D:\\ProjectData\\abc.jpg")
image=transform.scale(image,(5000,800))
class player:
    def __init__(self,x,y,vx,width,height,vy):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.width=width
        self.height=height
    def accelerate(self):
        p1.vx+=0.1

p1=player(700,400,1,80,80,2)
level=p1.y+p1.height
while run:
    for events in event.get():
        if events.type==QUIT:
            run=False
            break
    root.fill((0, 0, 0))
    root.blit(image,(x,y))
    draw.rect(root,(255,0,0),(p1.x,p1.y,p1.width,p1.height))
    keys=key.get_pressed()
    if keys[K_w] or isjump:
        isjump=True
        p1.y-=(g*dt)*1.2
        dt+=0.03
        if dt>5 and g>0:
            g=-g
            dt=0
        if dt>5 and g<0:
            g=-g
            dt=0
            isjump=False
    if keys[K_a] :
        #p1.x-=p1.vx
        x+=1
    if keys[K_d] :
        #p1.x+=p1.vx
        x-=1
    display.update()