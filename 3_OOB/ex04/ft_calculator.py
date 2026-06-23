class calculator:
    """
    Calculator class. Doesn't need __init__ as it
    only contains static methods
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Multiply items from same index in each vector and then
        add items from resulting list
        """
        result = sum(x * y for x, y in zip(V1, V2))
        print("Dot product is:", result)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add items from same index in each vector"""
        result = [float(x + y) for x, y in zip(V1, V2)]
        print("Add Vector is:", result)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract items in V2 from V1"""
        result = [float(x - y) for x, y in zip(V1, V2)]
        print("Sous Vector is:", result)
