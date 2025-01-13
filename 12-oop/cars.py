
class Car:
    def __init__(self, model, plate, max_speed, acceleration):
        self.model = model
        self.plate = plate 
        self.speed = 0
        self.max_speed = max_speed
        self.acceleration = acceleration

    def accelerate(self):
        if self.speed + self.acceleration <= self.max_speed:
            self.speed += self.acceleration
        else:
            self.speed = self.max_speed

    def slow_down(self):
        if self.speed - self.acceleration > 0:
            self.speed -= self.acceleration
        else:
            self.speed = 0

    def stop(self):
        self.speed = 0

    def print_status(self):
        if self.speed > 0:
            print(self.plate, "speed", self.speed)
        else:
            print(self.plate, "is stopped")

    def __str__(self):
        return self.plate + " speed: " + str(self.speed)


if __name__ == "__main__":
    a = Car("golf", "ZAA9098", 140, 10)
    b = Car("tesla", "ZAA1897", 180, 25)

    for i in range(5):
        a.accelerate()

    for i in range(40):
        b.accelerate()

    a.stop()
    a.print_status()
    b.print_status()