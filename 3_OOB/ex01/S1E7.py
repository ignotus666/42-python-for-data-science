from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family"""
    def __init__(self, first_name, is_alive=True):
        """Character constructor"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hair = 'dark'

    def die(self):
        """Method for killing the character"""
        self.is_alive = False

    def __str__(self):
        """Returns readable string, actually calls __repr__"""
        return (f"Vector: ('{self.family_name}', '{self.eyes}', \
                '{self.hair}')")

    def __repr__(self):
        """Returns representation for debugging"""
        return (f"Vector: ('{self.family_name}', '{self.eyes}' \
                            '{self.hair}')")


class Lannister(Character):
    """Representing the Lannister family"""
    def __init__(self, first_name, is_alive=True):
        """Character constructor"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hair = 'light'

    def die(self):
        """Method for killing the character"""
        self.is_alive = False

    def __str__(self):
        """Returns readable string, actually calls __repr__"""
        return (f"('{self.family_name}', '{self.eyes}', '{self.hair}')")

    def __repr__(self):
        """Returns representation for debugging"""
        return (f"Vector: ('{self.family_name}', '{self.eyes}' \
                            '{self.hair}')")

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Factory pattern returning an object to which
        we can potentially chain more methods
        """
        return cls(first_name, is_alive)
