class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        edu_status = "с высшим образованием" if self.higher_education else "без высшего образования"
        print(f"Привет! Меня зовут {self.name}. Я родился {self.birth_date}, "
              f"работаю {self.occupation}, {edu_status}.")

class Classmate(Person):
    def introduce(self):
        print(f"Привет! Меня зовут {self.name}, я одноклассник Эдиля. "
              f"Я родился {self.birth_date}, работаю {self.occupation}.")

class Friend(Person):
    def introduce(self):
        print(f"Привет! Меня зовут {self.name}, я друг Эдиля. "
              f"Я родился {self.birth_date}, работаю {self.occupation}.")

classmate1 = Classmate("Марат", "12.09.2006", "Экономист", True)
classmate2 = Classmate("Кутман", "23.06.2006", "Юрист", False)

friend1 = Friend("Даниель", "04.06.2008", "Финансист", True)
friend2 = Friend("Эмиль", "03.04.2006", "Программист", True)


for person in (classmate1, classmate2, friend1, friend2):
    person.introduce()