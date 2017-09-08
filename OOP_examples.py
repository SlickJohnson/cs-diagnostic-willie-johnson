class Car:
    number_of_wheels = 4
    make = "WJ20"
    model = "raC"
    color = "RED"
    top_speed = "9001"

    def __init__(self, color):
        self.color = color

    def honk():
        print("Beep Beep!")

    def descritipon(self):
        print("Number of wheels: ", self.number_of_wheels, "\nMake: ", self.make, "\nModel: ", self.model, "\nColor: ", self.color, "\nTop speed: ", self.top_speed)
