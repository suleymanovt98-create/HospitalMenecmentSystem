class Person:
    def __init__(self, name, surname, age, phone):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone

    def showInfo(self):
        print(f"Name:{self.name}\nSurname:{self.surname}\nAge:{self.age}\nPhone:{self.phone}")




# p = Person("Taleh", "Suleymanov", 29, "0501234567")
# p.showInfo()