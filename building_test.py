"""
Unit Test for the Building Class
"""

from building import Building


def describe_a_building():
    def that_has_a_name():
        king = Building("King")
        assert king.name == "King"
