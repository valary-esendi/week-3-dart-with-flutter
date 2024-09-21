

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"Vehicle Make: {self.make}, Model: {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def display_info(self):
        return f"{super().display_info()}, Doors: {self.doors}"


# Example Usage
car = Car("Mercedes-Benz", "Single-deck rigid bus", 3)
print(car.display_info())