from django.db import models

# BASE CLASS
class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    price = models.FloatField()

    def vehicle_info(self):
        return f"{self.brand} costs {self.price}"


# CHILD CLASS 1
class Car(Vehicle):
    doors = models.IntegerField()

    def vehicle_info(self):
        return f"{self.brand} Car with {self.doors} doors costs {self.price}"


# CHILD CLASS 2
class Motorcycle(Vehicle):
    helmet_included = models.BooleanField(default=True)

    def vehicle_info(self):
        return f"{self.brand} Motorcycle costs {self.price}"