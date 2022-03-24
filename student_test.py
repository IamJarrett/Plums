"""
Implements the student class which is a sub-class (or child class) of person
"""

# import the student class
from student import Student


def describe_a_student():
    def that_has_all_the_same_properties_as_a_person():
        bob = Student("bob", "Robertson", "bob@example.com")
        assert bob.first_name == "bob"
        assert bob.last_name == "Robertson"
        assert bob.email == "bob@example.com"

    def that_has_a_default_major_of_undecided():
        carl = Student("Carl", "Carlson", "carl@example.com")
        assert carl.major == "undecided"
