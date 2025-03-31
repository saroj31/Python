"""
This is used when we want to have a limited number of pool and want to use only that many objects and keep reusing the objects when needed.
"""

class Car:

    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model
        self.in_use = False


class CarPool:

    def __init__(self):
        self._available = []
        self._in_use = []

    def acquire_car(self)->Car:
        if len(self._available) == 0:
            self._available.append(Car("Ford","Mach E"))
        
        car = self._available.pop()
        self._in_use.append(car)
        car._in_use = True
        return car

    def release_car(self, car: Car) -> None:
        car.in_use = False
        self._in_use.remove(car)
        self._available.append(car)


if __name__ == "__main__":
    pool = CarPool()
    car_name = "Car 1"

    print(f"Acquire {car_name}")
    car1 = pool.acquire_car()
    print(f"{car_name} in use: {car1.in_use}")

    print(f"Now release {car_name}")
    pool.release_car(car1)
    print(f"{car_name} in use: {car1.in_use}")