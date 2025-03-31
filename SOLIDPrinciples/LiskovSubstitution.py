"""
By LIskov Substitution principle any superclass should be replacable with its subclass.
What I understand is if you override a method then make sure that even the superclass objects behaves in the same way as the subclass.

It ensures that, when using inheritance, subclasses extend their parent classes without altering their external behavior.
"""

# #Wrong Example of Liskov Substitution.
# class Bird:
#     def fly(self):
#         print("I can fly")

# class Penguin(Bird):

#     def fly(self):
#         print("I can't fly")

# def make_bird_fly(brd: Bird):
#     brd.fly()

# if __name__ == "__main__":

#     eagle = Bird()
#     penguin = Penguin()

#     make_bird_fly(eagle)
#     make_bird_fly(penguin)
    

# Correct way of having the behavior
class Bird:
    def move(self):
        print("I'm moving")

class FlyingBird(Bird):
    def move(self):
        print("I'm flying")

class FlightLessBird(Bird):
    def move(self):
        print("I'm walking")


#Same method for different behavior
def make_bird_move(bird: Bird):
    bird.move()


if __name__ == "__main__":
    generic_bird = Bird()

    eagle = FlyingBird()

    penguin = FlightLessBird()

    make_bird_move(generic_bird)
    make_bird_move(eagle)
    make_bird_move(penguin)
    