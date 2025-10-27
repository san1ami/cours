class Distance:
    UNIT_TO_METER = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }

    def __init__(self, value, unit):
        if unit not in self.UNIT_TO_METER:
            raise ValueError(f"Unsupported unit: {unit}")
        self.value = float(value)
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def to_meters(self):
        return self.value * self.UNIT_TO_METER[self.unit]

    def _create_with_same_unit(self, value_in_meters):
        return Distance(value_in_meters / self.UNIT_TO_METER[self.unit], self.unit)

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        result_meters = self.to_meters() + other.to_meters()
        return self._create_with_same_unit(result_meters)

    def __sub__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        result_meters = self.to_meters() - other.to_meters()
        if result_meters < 0:
            raise ValueError("Resulting distance cannot be negative!")
        return self._create_with_same_unit(result_meters)

    def __eq__(self, other):
        return self.to_meters() == other.to_meters()

    def __lt__(self, other):
        return self.to_meters() < other.to_meters()

    def __le__(self, other):
        return self.to_meters() <= other.to_meters()

    def __gt__(self, other):
        return self.to_meters() > other.to_meters()

    def __ge__(self, other):
        return self.to_meters() >= other.to_meters()


d1 = Distance(10, "m")
d2 = Distance(2, "km")
d3 = Distance(50, "cm")

print("Инициализация:")
print(d1, d2, d3)

print("\nСложение:")
print(d1, "+", d2, "=", d1 + d2)

print("\nВычитание:")
print(d2, "-", d1, "=", d2 - d1)

print("\nСравнение:")
print("10m == 1000cm? ->", Distance(10, "m") == Distance(1000, "cm"))
print("2km > 1500m? ->", Distance(2, "km") > Distance(1500, "m"))

print("\nПопытка отрицательного результата:")
try:
    print(d1 - d2)
except Exception as e:
    print("Ошибка:", e)
