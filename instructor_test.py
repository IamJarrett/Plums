"""
Unit test for instructor class
"""

from instructor import Instructor


def describe_an_instructor():
    def that_has_all_the_same_properties_as_a_person():
        david = Instructor("David", "Davidson", "bob@example.com", "A1")
        assert david.first_name == "David"
        assert david.last_name == "Davidson"
        assert david.email == "bob@example.com"

    def that_has_an_office():
        ernie = Instructor("Ernie", "Ernieson", "ernie@example.com", "King123")
        assert ernie.office == "King123"

    def that_has_a_display_name():
        francis = Instructor("Francis", "Franker", "frank@example.com", "King555")
        francis.first_name == "frank"
        assert francis.last_name == "Franker"
        assert francis.email == "frank@example.com"
