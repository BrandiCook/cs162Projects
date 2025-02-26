# Author: Brandi Cook
# Date: 9/27/2020
# Description: This program finds the mean median and mode of given ages of people

import statistics


class Person:
    """
    Represents a person. Contains methods for
    getting name and age
    """

    def __init__(self, name, age):
        """ Returns a person object with the given name and age"""
        # Leading with an underscore indicates
        # that the name and age are intended to be private
        self._name = name
        self._age = age

    def get_name(self):
        """Returns the name of the Person"""
        return self._name

    def get_age(self):
        """Returns the age of the Person"""
        return self._age


def basic_stats(l):
    ages = []
    for i in range(0, len(l)):
        print(l[i].get_name() + " " + str(l[i].get_age()))
        ages.append(l[i].get_age())
    return (statistics.mean(ages), statistics.median(ages), statistics.mode(ages))


"""
p1 = Person("Kyoungmin", 73)
p2 = Person("Mercedes", 24)
p3 = Person("Avanika", 48)
p4 = Person("Marta", 24)

person_list = [p1, p2, p3, p4]
# basic_stats(person_list)
print(basic_stats(person_list))  # should print a tuple of three values
"""