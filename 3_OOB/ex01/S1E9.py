from abc import ABC, abstractmethod


class Character(ABC):
    """Base class for characters"""
    def __init__(self, first_name, is_alive=True):
        """Character constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract (template) method to kill the character"""
        pass


class Stark(Character):
    """Stark inherits from Character"""
    def __init__(self, first_name, is_alive=True):
        """Constructor; is_alive defaults to True"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Method for killing the character"""
        self.is_alive = False
