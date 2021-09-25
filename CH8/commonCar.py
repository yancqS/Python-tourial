from battery import Battery


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.meter = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def get_meter(self):
        print(f"This car has {self.meter} miles on it")

    def update_meter(self, meter):
        if meter > self.meter:
            self.meter = meter
        else:
            print("You can't roll back an meter")

    def increment_meter(self, miles):
        self.meter += miles


class EcarSec(Car):
    def __init__(self, make, model, year, battery):
        super().__init__(make, model, year)
        self.battery = Battery(battery)

    def get_descriptive_name(self):
        long_name = f"e_car info: {self.year} {self.make} {self.model}"
        return long_name

