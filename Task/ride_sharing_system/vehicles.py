"""Vehicles for the Ride Sharing System.

Vehicle is an abstract class (the plan).
Bike and Car are the real vehicles, each with its own fare rule.
"""

from abc import ABC, abstractmethod

from exceptions import InvalidRatingError, InvalidDistanceError


class Vehicle(ABC):
    vehicle_type = "Vehicle"      # each child changes this

    def __init__(self, driver_name, rating):
        self.driver_name = driver_name
        self.rating = rating      # goes through the rating setter below

    # ---------- rating: getter and setter with @property ----------
    #
    # GETTER = a method that GIVES a value out.
    # SETTER = a method that CHANGES a value, but CHECKS it first.
    #
    # Before (Day 19), we wrote getter and setter as normal methods:
    #
    #     def get_rating(self):
    #         return self.__rating
    #
    #     def set_rating(self, value):
    #         if value < 1 or value > 5:
    #             print("Rating must be between 1 and 5")
    #         else:
    #             self.__rating = value
    #
    #     car.set_rating(4)          # change: call a method
    #     print(car.get_rating())    # read:   call a method, with ()
    #
    # Now we use @property. The checking is the same,
    # but we use it like a normal variable:
    #
    #     car.rating = 4             # Python runs the setter below
    #     print(car.rating)          # Python runs the getter below, no ()
    #
    # How it is different from get_ / set_:
    #   1. One name, "rating", for both. Not get_rating and set_rating.
    #   2. Read with car.rating, change with car.rating = 4. No brackets.
    #   3. Nobody can skip the check: even car.rating = 10
    #      goes through the setter and is stopped.
    #   4. __init__ also uses the setter (self.rating = rating above),
    #      so a vehicle with a bad rating can't even be made.
    #   5. A bad value RAISES an error instead of only printing,
    #      so main.py can catch it with try / except.
    #
    # The real value is saved in self._rating (with an underscore).
    # Inside the getter and setter, always use self._rating.
    # If the setter wrote self.rating = value, it would call itself
    # again and again forever (RecursionError).

    @property
    def rating(self):                 # GETTER: runs on  print(car.rating)
        return self._rating

    @rating.setter
    def rating(self, value):          # SETTER: runs on  car.rating = 4
        if value < 1 or value > 5:
            raise InvalidRatingError("Rating must be between 1 and 5.")
        self._rating = value

    # ---------- common check for every vehicle ----------
    def check_distance(self, distance):
        if distance <= 0:
            raise InvalidDistanceError("Distance must be more than 0 km.")

    # ---------- every child MUST write this ----------
    @abstractmethod
    def calculate_fare(self, distance):
        pass

    def __str__(self):
        return f"{self.vehicle_type} driven by {self.driver_name} (rating {self.rating})"


class Bike(Vehicle):
    vehicle_type = "Bike"
    BASE_FARE = 25        # Rs. to start the ride
    PER_KM = 10           # Rs. for every km

    def calculate_fare(self, distance):
        self.check_distance(distance)
        return self.BASE_FARE + self.PER_KM * distance


class Car(Vehicle):
    vehicle_type = "Car"
    BASE_FARE = 60
    PER_KM = 20

    def calculate_fare(self, distance):
        self.check_distance(distance)
        return self.BASE_FARE + self.PER_KM * distance
