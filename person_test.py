"""
Unit tests for the Person class
"""

# import the code to be tested
from person import Person


def describe_a_person():
    def that_has_a_first_name_and_last_name_and_email_address():
        alice = Person("alice", "alison", "alice@example.com")
        assert alice.first_name == "alice"
        assert alice.last_name == "alison"
        assert alice.email == "alice@example.com"
