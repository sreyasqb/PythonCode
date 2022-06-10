class player:
    x=0
    vel=1
    @classmethod
    def moveRight(self):
        self.x+=self.vel
    @classmethod
    def moveLeft(cls):
        cls.x-=cls.vel



p1=player
while True:
    p1.moveLeft()
    print(p1.x)

