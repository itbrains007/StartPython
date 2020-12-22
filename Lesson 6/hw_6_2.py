
class Road:

    def __init__(self, length, width):
        self._lenght= length
        self._width = width

    def mass(self):
        return self._width*self._lenght*25*5

road = Road(3,2)
print(road.mass())