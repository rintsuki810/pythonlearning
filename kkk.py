class Head:
    def __init__(self,size):
        self.size=size

class Body:
    def __init__(self,capacity):
        self.capacity=capacity
        
class Hand:
    def __init__(self,length):
        self.length=length

class Leg:
    def __init__(self,width):
        self.width=width

class People:
    def __init__(self):
        self.hd=None
        self.by=None
        self.rh=None
        self.lh=None
        self.rl=None
        self.ll=None

handsome=People()
handsome.hd=Head(20)
print(handsome.hd.size)
handsome.by=Body(50)
handsome.rh=Hand(30)
handsome.lh=Hand(35)
handsome.rl=Leg(75)
handsome.ll=Leg(70)

hsu=People()
hsu.hd=Head(25)
print(handsome.hd.size)
hsu.by=Body(48)
hsu.rh=Hand(25)
hsu.lh=Hand(25)
hsu.rl=Leg(75)
hsu.ll=Leg(70)

swap=hsu
handsome=hsu
swap=handsome
print(handsome.hd.size)