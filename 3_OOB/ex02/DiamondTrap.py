from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    @property
    def eyes(self):
        """Getter: accessing Joffrey.eyes will run this"""
        return self.__dict__.get('eyes')

    @eyes.setter
    def eyes(self, colour):
        """Setter: assigning Joffrey.eyes = 'colour' will run this"""
        self.__dict__['eyes'] = colour

    @property
    def hair(self):
        """Getter: accessing Joffrey.hair will run this"""
        return self.__dict__.get('hair')

    @hair.setter
    def hair(self, colour):
        """Setter: assigning Joffrey.hair = 'colour' will run this"""
        self.__dict__['hair'] = colour

    def get_eyes(self):
        """Makes it compatible with the tester method"""
        return self.eyes

    def set_eyes(self, colour):
        """Makes it compatible with the tester method"""
        self.eyes = colour

    def get_hair(self):
        """Makes it compatible with the tester method"""
        return self.hair

    def set_hair(self, colour):
        """Makes it compatible with the tester method"""
        self.hair = colour
