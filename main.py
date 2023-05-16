class Student:
    def __init__(self):
        self.name = "Zain"
        self.grades = (1, 2, 4, 6, 7, 8)

    def averageGrade(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Person({self.name}, {self.grades})"

    def __repr__(self):
        return f"<Person({self.name}, {self.grades})>"


student1 = Student()
print(student1.averageGrade())


class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        self.items.append({
            "name": name,
            "price": price
        })

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        total = 0
        for item in self.items:
            total += item["price"]
        return total


newStock = Store("bitcoin")
newStock.add_item("btc", 45)
newStock.add_item("btc-eth", 78)
print(newStock.stock_price())


class ClassTest:
    Types = ["Novel", "Journal"]

    def instance_method(self):
        return f"This is calling class method for instance {self}"

    @classmethod
    def class_method(cls):
        return f"This is calling class method {cls}"

    @staticmethod
    def static_method():
        return f"this is a static method"


inst = ClassTest()
print(inst.instance_method())
print(ClassTesflaskt.class_method())
ClassTest.static_method()

print(ClassTest.Types)
