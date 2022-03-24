"""
Unit tests for room class
"""

from room import Room


def describe_a_room():
    def that_has_a_number_length_width_and_capacity():
        """
        A room has a room number, a size (in squared feet)
        and a person capacity limit
        """
        my_office = Room("123", 10, 10)
        assert my_office.number == "123"
        assert my_office.length == 10
        assert my_office.width == 10
        assert my_office.capacity == 5
        assert my_office.size == 100

        a_classroom = Room("564", 50, 50)
        assert a_classroom.number == "564"
        assert a_classroom.length == 50
        assert a_classroom.width == 50
        assert a_classroom.capacity == 125
        assert a_classroom.size == 2500
