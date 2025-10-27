class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

# Создание экземпляров класса
person1 = Person("Алексей", "1990-05-14", "Инженер", True)
person2 = Person("Мария", "1995-09-21", "Дизайнер", False)
person3 = Person("Иван", "1988-12-03", "Учитель", True)

# Печать атрибутов каждого экземпляра
for person in (person1, person2, person3):
    print(f"Имя: {person.name}")
    print(f"Дата рождения: {person.birth_date}")
    print(f"Профессия: {person.occupation}")
    print(f"Высшее образование: {person.higher_education}")
    print("-" * 30)