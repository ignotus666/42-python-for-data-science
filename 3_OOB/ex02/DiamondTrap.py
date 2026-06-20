from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        return (self.eyes)
    
    def set_eyes(self, colour):
        self.eyes = colour

    def get_hair(self):
        return (self.hair)
    
    def set_hair(self, colour):
        self.hair = colour