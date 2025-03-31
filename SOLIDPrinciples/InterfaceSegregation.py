"""
Interface should be separated to simpler or smaller dependent units.
Any class who wants to use the interface should have the choice to pick and choose their interfaces.
"""

from typing import Protocol

# By INterface Segregation principle(ISP) separated the interface to small parts
class Printer(Protocol):
    def print_document(self):
        ...

class Scanner(Protocol):
    def scan_document(self):
        ...

class Fax(Protocol):
    def fax_document(self):
        ...

class AllInOnePrinter():

    def print_document(self):
        print("Printing")

    def scan_document(self):
        print("Scanning")

    def fax_document(self):
        print("Faxing")

# can make this because of ISP
class OnlyPrinter():

    def print_document(self):
        print("Only Printing")

def print_action(printer: Printer):
    printer.print_document()

if __name__ == "__main__":

    all_in_one = AllInOnePrinter()
    all_in_one.scan_document()
    all_in_one.fax_document()
    all_in_one.print_document()

    only_printer = OnlyPrinter()
    only_printer.print_document()