def organise(d):
    m=max(d.keys())
    for i in range(m,-1,-1):
        if i not in d.keys():
            d[i]=0
    return d

class Polynomial:
    def __init__(self,poly):
        self.poly=organise(poly)
        self.deg=max(poly.keys())
    def __str__(self):
        s=""
        for i in range(self.deg,-1,-1):
            if self.poly[i]!=0:
                s+=" + " + str(self.poly[i])+"*x^"+str(i)
        return s
    def __add__(self, obj):
        d={}
        for i in range(max(self.deg,obj.deg),-1,-1):
           if i in self.poly and i in obj.poly:
               d[i]=self.poly[i]+obj.poly[i]
           elif i in self.poly and i not in obj.poly:
               d[i]=self.poly[i]
           elif i in obj.poly and i not in self.poly:
               d[i]=obj.poly[i]
        return Polynomial(d)
    def __sub__(self, obj):
        d={}
        for i in range(max(self.deg,obj.deg),-1,-1):
           if i in self.poly and i in obj.poly:
               d[i]=self.poly[i]-obj.poly[i]
           elif i in self.poly and i not in obj.poly:
               d[i]=self.poly[i]
           elif i in obj.poly and i not in self.poly:
               d[i]=obj.poly[i]
        return Polynomial(d)
    def __eq__(self, obj):
        if self.deg==obj.deg:
            for i in range(self.deg,-1,-1):
                if self.poly[i]!=obj.poly[i]:
                    return False
        else:
            return False
        return True




d1={4:1,0:1}
d2={5:2,2:1}
p1=Polynomial(d1)
p2=Polynomial(d2)
print(p1)
print(p2)
print(p1+p2)
print(p1-p2)
print(p1==p2)







