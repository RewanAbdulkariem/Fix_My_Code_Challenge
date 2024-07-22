#!/usr/bin/python3
"""
This class represents a user with an email attribute.
"""


class User():
    """ User class for managing user data."""

    def __init__(self):
        """ Initialize a new User instance with no email address. """
        self.__email = None

    @property
    def email(self):
        """ Get the email address of the user. """
        return self.__email

    @email.setter
    def email(self, value):
        """ Set the email address of the user."""
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":
    """ main to run"""
    u = User()
    u.email = "john@snow.com"
    print(u.email)
