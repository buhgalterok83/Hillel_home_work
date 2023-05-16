class Car:
    """Клас автомобіля."""

    num_wheels = 4  # классове поле

    def __init__(self, make, model, year, weight):
        """Ініціалізація атрибутів машини."""
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.is_running = False

    def start(self):
        """Завести автомобіль."""
        if not self.is_running:
            self.is_running = True
            print(f"The {self.make} {self.model} is now running.")

    def stop(self):
        """Зупинити автомобіль."""
        if self.is_running:
            self.is_running = False
            print(f"The {self.make} {self.model} has been stopped.")

    @classmethod
    def get_num_wheels(cls):
        """Повертає кількість коліс у класі автомобіля."""
        return cls.num_wheels

    @staticmethod
    def convert_weight_to_pounds(weight_in_kg):
        """Конвертує вагу автомобіля з кілограмів в фунти."""
        return weight_in_kg * 2.20462


class Driver:
    """Клас водія."""

    def __init__(self, name, age, driving_experience):
        """Ініціалізуємо атрибути водія."""
        self.name = name
        self.age = age
        self.driving_experience = driving_experience

    def start_car(self, car):
        """Завести авто."""
        car.start()

    def stop_car(self, car):
        """Зупинити авто."""
        car.stop()


# Створюємо екземпляри класів
car1 = Car("Toyota", "Corolla", 2022, 1200)
car2 = Car("Honda", "Accord", 2022, 1400)
driver1 = Driver("John", 30, 10)
driver2 = Driver("Anna", 25, 5)

# Взаємодія з об'єктами
driver1.start_car(car1)
driver2.start_car(car2)
driver1.stop_car(car1)
driver2.stop_car(car2)

# Виклик методу класу
print(Car.get_num_wheels())  # Виведе: 4

# Виклик статичного методу
weight_in_kg = 1200
weight_in_pounds = Car.convert_weight_to_pounds(weight_in_kg)
print(f"The weight of the car is {weight_in_pounds} pounds.")  # Виведе: The weight of the car is 2645.5474 pounds.
