"""
BY this principle, it emphasizes that the osftware entities(classes) should be open for extension but closed for modification inside the entity.
This makes sense as this makes the application more robust and will introduce less bugs. The base code always works and you can add extensions or
interfaces or inheritance to extend new features.

I will add a point is after the software becomes stable this makes sense.We shoudl wait until the software becomes stable.
"""

# Below is a Rectangle example adhering to this principle

import math
from typing import Protocol

class Shape(Protocol):

    def area(self) -> float:
        ...

class Rectangle:

    def __init__(self, length: float, breadth: float):
        self.length = length
        self.breadth = breadth

    def area(self) -> float:
        return self.breadth * self.length
    

class Circle:

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius * self.radius
    
def calculate_area(polygon: Shape):

    return polygon.area()


if __name__ == "__main__":

    one_rect = Rectangle(2.1, 3)

    one_circ = Circle(3)

    print(f"Rectangle area: {calculate_area(one_rect)}.")

    print(f"Circle area: {calculate_area(one_circ)}")
