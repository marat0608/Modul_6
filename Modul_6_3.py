import random


class Animal:
    live = True
    sound = None # - звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0
    _cords = [0, 0, 0]
    def __init__(self, speed):
        self.speed = speed
    def move(self, dx, dy, dz):
        self._cords = [dx*self.speed, dy*self.speed, dz*self.speed]
        if self._cords[2] < 0:
            print("It's too deep, i can't dive :(")
    def get_cords(self):
        return print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")
    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True
    def lay_eggs(self):
        egg = random.randint(1,4)
        print(f"Here are(is) {egg} eggs for you")
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 5

    def dive_in(self, dz):
        self._cords[2] = abs(int(self._cords[2]) // int(self.speed)) - dz // 2


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"

db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(1)
db.get_cords()
db.lay_eggs()

print(Duckbill.mro())



