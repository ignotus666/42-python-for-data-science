class calculator:
    """Calculator class"""
    def __init__(self, vector):
        """Calculator constructor"""
        self.vector = vector

    def __add__(self, scalar) -> None:
        """Add scalar to each vector item"""
        self.vector = [x + scalar for x in self.vector]
        print(self.vector)

    def __mul__(self, scalar) -> None:
        """Multiply each vector item by scalar"""
        self.vector = [x * scalar for x in self.vector]
        print(self.vector)

    def __sub__(self, scalar) -> None:
        """Subtract scalar from each vector item"""
        self.vector = [x - scalar for x in self.vector]
        print(self.vector)

    def __truediv__(self, scalar) -> None:
        """Divide each vector item by scalar"""
        if scalar == 0:
            print("Error: can't divide by zero")
            return
        self.vector = [x / scalar for x in self.vector]
        print(self.vector)
