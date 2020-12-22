from time import sleep

class TrafficLight:
    __color = ""

    def running(self):
        for __color in ("red","yellow","green"):
            print(__color)
            if __color == "red":
                sleep(7)
            elif __color == "yellow":
                sleep(2)
            else:
                sleep(7)

tl=TrafficLight()
tl.running()