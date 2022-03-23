"""
Defines the person class that will be the base class 
for students and instructors
"""


class Person:
    """
    The Person class is the base class for defining
    all people in the Plums, including students,
    instructors, and capture all of the basic
    properties common to both of these subclasses.
    """

    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email_address
