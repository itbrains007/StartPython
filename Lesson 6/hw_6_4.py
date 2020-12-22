class Car:
    def __init__ ( self, speed, color, name, is_police ):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go ( self ):
        print ("Поехали!!!")

    def stop ( self ):
        print ("Стоп")

    def turn ( self, derection ):
        print (f"Поворот на/в {derection}")

    def show_speed ( self ):
        print (f"Скорость авто: {self.speed}")


class TownCar (Car):
    def __init__ ( self, speed, color, name, is_police, childseat ):
        super ().__init__ (speed, color, name, is_police)
        self.childseat = childseat

    def show_speed ( self ):
        if self.speed > 60:
            print (f"Скорость авто: {self.speed} и Вы превышаете")
        else:
            print (f"Скорость авто: {self.speed}")

class WorkCar(Car):
    def __init__ ( self, speed, color, name, is_police, tonn):
        super ().__init__ (speed, color, name, is_police)
        self.tonn = tonn

    def show_speed ( self ):
        if self.speed > 40:
            print (f"Скорость авто: {self.speed} и Вы превышаете")
        else:
            print (f"Скорость авто: {self.speed}")


class SportCar (Car):
    def __init__ ( self, speed, color, name, is_police, wheel ):
        super ().__init__ (speed, color, name, is_police)
        self.wheel = wheel

    def show_speed ( self ):
        if self.speed < 90:
            print (f"Скорость авто: {self.speed} и стоит прибавить")
        else:
            print (f"Скорость авто: {self.speed}")

sportcar = SportCar (45, "red", "BMW", False, 225)
sportcar.go ()
sportcar.turn ("лево")
sportcar.go ()
print(f"Марка авто: {sportcar.name}.")
sportcar.show_speed()
sportcar.stop ()

towncar = TownCar (61, "red", "Chevrole", False, True)
print(f"Марка авто: {towncar.name}. Цвет: {towncar.color}")
if towncar.childseat == True:
    print(f"В машине есть детское сидение")
towncar.show_speed ()

policecar= Car(50, "red", "Ford", True)
if policecar.is_police == True:
    print(f"Это полицейская машина. Марка: {policecar.name}. Цвет: {policecar.color}")