import threading, time


class Vehicle(threading.Thread):
    def __init__(self, type):
        super().__init__()
        self.type = type
        self.fuel = 50
        self.km_traveled = 0
        if type == "truck":
            self.consumption = 12
            self.speed = 1

        else:
            self.consumption = 12
            self.speed = 1.6

    def run(self):
        while True:
            time.sleep(self.speed)
            if self.fuel <= self.consumption + 0.01:
                print(f"Refilling {self.type} tank...")
                time.sleep(4)
                self.fuel = 50
            else:
                self.fuel -= self.consumption
                self.km_traveled += 100 * self.speed
                print(f"{self.type} is running ({self.fuel:.2f}) , km traveled: {self.km_traveled}")


car = Vehicle("truck")
truck = Vehicle("car")

car.start()
truck.start()
