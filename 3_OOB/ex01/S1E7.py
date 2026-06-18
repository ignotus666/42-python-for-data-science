from S1E9 import Character


class Baratheon(Character):
    """Baratheon family class"""
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
        return (f"('{self.family_name}', '{self.eyes}', '{self.hair}')")

    def __repr__(self):
        """Returns representation for debugging"""
        return (f"Vector: ('{self.family_name}', '{self.eyes}' \
                            '{self.hair}')")


class Lannister(Character):
    """Lannister family class"""
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
        """Shows what print/str outputs"""
        return (f"Vector: ('{self.family_name}', '{self.eyes}' \
                            '{self.hair}')")

    def __repr__(self):
        """Shows what repr outputs"""
        return (f"Vector: ('{self.family_name}', '{self.eyes}' \
                            '{self.hair}')")
