class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car1.name = "lexus"
car1.kind = "car"
car1.color = "white"
car1.value = 100.00

car2 = Vehicle()
car2.name = "toyota"
car2.kind = "bus"
car2.color = "blue"
car2.value = 400.00
# test code
print(car1.description())
print(car2.description())