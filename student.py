"""
Describes a student in the PLuMS enviorment
"""

# import the parent class from Student
from person import Person


class Student(Person):
    def __init__(self, first_name, last_name, email_address, major="undecided"):
        Person.__init__(self, first_name, last_name, email_address)
        self.major = major
