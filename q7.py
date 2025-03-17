# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 03:30:41 2025

@author: zacha
"""

class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """

    def __init__(self, make ,model ,year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")


# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020

x = Car("Toyota","Corolla",2020)
x.describe_car()
# Ans: 2020 Toyota Corolla