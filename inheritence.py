from typing import  List
class Device:
    def __init__(self, name:str, connect_by:str):
        self.name = name
        self.connect_by = connect_by
        self.connected = True

    def __str__(self) -> str:
        return f"{self.name!r} printer, connected by {self.connect_by}"

    def disconnect(self):
        print("disconnected successfuly")
        self.connected = False


class Printer(Device):
    def __init__(self, name, connect_by, capacity):
        super().__init__( name, connect_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"({super().__str__()}) remaining ({self.remaining_pages}) remaining pages.)"

    def print(self, pages):
        if not self.connected:
            print("You are not connected ")
            return

        if self.remaining_pages == 0:
            print("Out of Pages")

        self.remaining_pages -= pages
        print(f"Printed {pages} Pages Remaining Left 0")


printer1 = Printer("Hp-Lazer","PC",50)
print(printer1.remaining_pages)
printer1.print(50)
print(printer1.remaining_pages)
printer1.print(50)