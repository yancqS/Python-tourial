class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def get_bettery(self):
        print(f"This car has a {self.battery_size}-kwh battery")