
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

    """
    GITHUB TEST
    """