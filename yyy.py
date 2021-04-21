class Person:
    def __init__(self,name,weight,hp,ap):
        self.name=name
        self.weight=weight
        self.hp=hp
        self.ap=ap

    def eat(self,valume):
        self.weight+=valume

    def exercise(self):
        self.weight-=1

    def underattack(self,who):
        self.hp-=  who.ap
    
    def attack(self,who):
        who.hp-=self.ap

handsome=Person("伍雯琪",50,1000,200)
hsu=Person("徐淑芳",48,1000,150)
print(handsome)
print(handsome.name)
print(handsome.weight)
handsome.eat(10)
print(handsome.weight)
print(handsome.hp)
handsome.underattack(hsu)
print(handsome.hp)



print(hsu)
print(hsu.name)
print(hsu.weight)
hsu.exercise()
print(hsu.weight)
hsu.attack(handsome)
print(handsome.hp)