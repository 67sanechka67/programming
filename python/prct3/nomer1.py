class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


class Developer(Employee):
    def __init__(self, name, base_salary, overtime_hours, hourly_rate):
        super().__init__(name, base_salary)
        self.overtime_hours = overtime_hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.base_salary + (self.overtime_hours * self.hourly_rate)


# Пример использования:
emp = Employee("Анна", 50000)
mgr = Manager("Иван", 80000, 25000)
dev = Developer("Олег", 90000, 10, 1500)

print(f"{emp.name}: {emp.calculate_salary()} руб.")  # 50000 руб.
print(f"{mgr.name}: {mgr.calculate_salary()} руб.")  # 105000 руб.
print(f"{dev.name}: {dev.calculate_salary()} руб.")  # 105000 руб.