"""
Unit tests for room class
"""
from room import floor
from building import Building
from room import SQFT_PER_PERSON, Room


def describe_a_room():
    def that_has_a_building_number_length_width_and_capacity():
        """
        A room has a room number, a size (in squared feet)
        and a person capacity limit
        """
        engeo = Building("EnGeo")
        king = Building("King")

        my_office = Room(engeo, "123", 10, 10)
        assert my_office.number == "123"
        assert my_office.length == 10
        assert my_office.width == 10
        assert my_office.capacity == 5
        assert my_office.size == 100
        expected_capacity = floor(my_office.size / SQFT_PER_PERSON)
        assert my_office.name == "EnGeo 123"

        a_classroom = Room(king, "564", 50, 50)
        assert a_classroom.number == "564"
        assert a_classroom.length == 50
        assert a_classroom.width == 50
        assert a_classroom.capacity == 125
        assert a_classroom.size == 2500
        expected_capacity = floor(a_classroom.size / SQFT_PER_PERSON)
        assert a_classroom.capacity == expected_capacity
        assert a_classroom.name == "King 564"
