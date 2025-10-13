class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    def introduce(self):
        edu_status = "у меня есть высшее образование" if self.higher_education else "у меня нет высшего образования"
        print(f"Привет! Меня зовут {self.name}. "
              f"Моя профессия — {self.occupation}. "
              f"{edu_status}.")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group = group

    def introduce(self):
        edu_status = "у меня есть высшее образование" if self.higher_education else "у меня нет высшего образования"
        print(f"Привет, меня зовут {self.name}. "
              f"Моя профессия — {self.occupation}. "
              f"Я учился с Эдил в группе {self.group}. "
              f"{edu_status}.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        edu_status = "у меня есть высшее образование" if self.higher_education else "у меня нет высшего образования"
        print(f"Привет, меня зовут {self.name}. "
              f"Моя профессия — {self.occupation}. "
              f"Мое хобби — {self.hobby}. "
              f"{edu_status}.")


# Создание объектов с правильным количеством аргументов
classmate1 = Classmate("Марат", "12.09.2006", "Экономист", True, "7-Б")
classmate2 = Classmate("Кутман", "23.06.2006", "Юрист", False, "9-А")

friend1 = Friend("Даниель", "04.06.2008", "Финансист", True, "чтение")
friend2 = Friend("Эмиль", "03.04.2006", "Программист", True, "геймер")

# Пример вывода
classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()


