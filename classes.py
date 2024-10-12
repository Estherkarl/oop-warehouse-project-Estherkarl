
from datetime import datetime

class Item:
    def __init__(self, state: str, category: str, warehouse: int, date_of_stock: datetime):
        self.state = state
        self.category = category
        self.date_of_stock = date_of_stock
        self.warehouse = warehouse  # Ensure warehouse is tracked with each item

    def __str__(self):
        return f"{self.state} - {self.category} (Warehouse: {self.warehouse})"

class Warehouse:
    def __init__(self, warehouse_id: int):
        self.id = warehouse_id
        self.stock = []  # Initialize an empty stock list

    def occupancy(self) -> int:
        return len(self.stock)

    def add_item(self, item: Item):
        self.stock.append(item)  # Add item to the stock

    def search(self, search_term: str):
        return [item for item in self.stock if search_term in item.category or search_term in item.state]

class User:
    def __init__(self, user_name: str):
        self._name = user_name if user_name else "Anonymous"
        self.is_authenticated = False

    def authenticate(self, password: str) -> bool:
        return False  # Standard users can't authenticate

    def is_named(self, name: str) -> bool:
        return self._name == name

    def greet(self):
        print(f"Hello, {self._name}!")
        print("Welcome to our Warehouse Database.")
        print("If you don't find what you are looking for,")
        print("please ask one of our staff members to assist you.")

    def bye(self):
        print(f"Thank you for your visit, {self._name}!")

class Employee(User):
    def __init__(self, user_name: str, password: str, head_of: list = None):
        super().__init__(user_name)
        self.__password = password
        self.head_of = head_of if head_of else []

    def authenticate(self, password: str) -> bool:
        return password == self.__password  # Authenticate employee

    def order(self, item: Item, amount: int):
        print(f"Ordered {amount} of {item}.")

    def greet(self):
        print(f"Hello, {self._name}!")
        print("If you experience a problem with the system,")
        print("please contact technical support.")

    def bye(self, actions: list):
        super().bye()  # Call the parent bye method
        print("Summary of actions taken during your session:")
        for action in actions:
            print(action)
