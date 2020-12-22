
class Woker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Woker):
    def get_full_name(self):
        return self.name+ " "+ self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

position = Position("Ivan", "Petrov", "Programmer", 100000, 50000)
print(position.get_full_name())
print(position.get_total_income())