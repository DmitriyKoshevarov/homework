import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed, _cords = [0, 0, 0]):
        self.speed = speed
        self._cords = _cords

    def move(self, dx, dy, dz):
        if dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] = dx * self.speed
            self._cords[1] = dy * self.speed
            self._cords[2] = dz * self.speed

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    def __init__(self, speed: float):
        super().__init__(speed)
        self.beak = True

    def lay_eggs(self):
        eggs_count = random.randint(1, 4)
        if eggs_count > 1:
            print(f"Here are {eggs_count} eggs for you.")
        else:
            print(f"Here is {eggs_count} eggs for you.")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def __init__(self, speed: float):
        super().__init__(speed)

    def dive_in(self, dz: float):
        self._cords[2] -= abs(dz) * (self.speed/2)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

    def __init__(self, speed: float):
        super().__init__(speed)

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"
    def __init__(self, speed):
        super().__init__(speed)

db = Duckbill(10)

print(db.live)
print(db.beak)
db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()