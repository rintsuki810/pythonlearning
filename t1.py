class Engine:
    def __init__(self,cc):
        self.cc=cc

class Wheel:
    def __init__(self,size):
        self.size=size

class Car:
    def __init__(self,name,cc,size):
        self.name=name
        self.eg=Engine(cc)
        self.f1=Wheel(size)
        self.f2=Wheel(size)
        self.b1=Wheel(size)
        self.b2=Wheel(size)

bmw=Car("bmw",6600,40)
