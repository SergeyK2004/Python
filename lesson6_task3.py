class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            "wage": wage,
            "bonus": bonus
        }

    def info(self):
        print(self.name, self._income)


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return(self.name + ' ' + self.surname)

    def get_total_income(self):
        return(self._income["wage"] + self._income["bonus"])


a = Position("Ivan", "Petrov", "director", 250000, 10000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())
