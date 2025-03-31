class Circle:
    def __init__(self, radius: int):
        self._radius: int = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, in_radius:int):
        if in_radius < 0:
            raise ValueError("radius cannot be negative")
        
        self._radius = in_radius
    

if __name__ == "__main__":

    cir = Circle(10)

    print(f"initial radius = {cir.radius}")

    cir.radius = 13

    print(f"updated radius = {cir.radius}")


    