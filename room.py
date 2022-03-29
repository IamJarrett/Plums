"""
Implements the Room class for the PLuMS system
"""

from math import floor

SQFT_PER_PERSON = 20


class Room:
    """
    A location where things take place. Could be
    an office, classroom, etc.
    """

    def __init__(self, building, number, length, width):
        self.building = building
        self.number = number
        self.length = length
        self.width = width

    @property
    def size(self):
        return self.length * self.width

    @property
    def capacity(self):
        return self.size / SQFT_PER_PERSON

    @property
    def name(self):
        return f"{self.building.name} {self.number}"
