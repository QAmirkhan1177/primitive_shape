class Polygon:
    def __init__(self, a,b) -> None:
        self.a = a
        self.b = b

    def getArea(self):
        """
        This method finds the area of the Polygon.

        Args:
            No
        Returns:
            float or int: return perimeter of the polygon.
        """
        return self.a*self.b

    def getPerimeter(self):
        """
        This method finds the perimeter of the Polygon.

        Args:
            No
        Returns:
            float or int: return perimeter of the polygon.
        """
        return 2*(self.a+self.b)
answer=Polygon(4,6)
print(answer.getArea())