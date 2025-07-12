class Car:
    def __init__(self, colour, type, year):
        self.colour = colour
        self.type = type
        self.year = year
    def ignition(self):
        print("Автомобиль заведен")
    def shutdown(self):
        print("Автомобиль заглушен")
    def establish_colour(self, colour):
        self.colour = colour
        print(colour)
    def establish_type(self, type):
        self.type = type
        print(type)
    def establish_year(self, year):
        self.year = year
        print(year)

car = Car("red", "fuck", "hz")
car.establish_colour(input())
car.establish_type(input())
car.establish_year(input())