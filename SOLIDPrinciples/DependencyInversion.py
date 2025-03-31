"""
Here it suggests we should not let a HIgh-Level class depend on a low level class.
Instead of that we should make interface classes and inherit those inteface class to the dependent classes.

This geenrally does not bring interdepndency of classes and makes the system loosely coupled. The higher level objects also do not 
need to keep all the implementation of the low level objects.
"""

from typing import Protocol

class MessageSender(Protocol):
    def send(self,message: str):
        ...

class Email():
    def send(self, message: str):
        print(f"sending email: {message}")

class Notification():
    # Here notification only has the interface MessageSender
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def send(self, message: str):
        self.sender.send(message=message)


if __name__ == "__main__":
    email = Email()
    notif = Notification(sender=email)

    notif.send(message="meesage here")