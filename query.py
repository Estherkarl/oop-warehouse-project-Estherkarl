from loader import Loader
from classes import User

# Load personnel and stock data
personnel_loader = Loader(model="personnel")
stock_loader = Loader(model="stock")

# User interaction
user_name = input("Enter your name: ")
user = User(user_name)

# Greet the user
user.greet()

# Check if the user is an employee
for emp in personnel_loader:
    if emp.is_named(user_name):
        user = emp  # If an employee, replace the user with Employee instance
        break

# Main interaction loop
actions = []
while True:
    command = input("Enter a command (search, exit): ")
    if command == "search":
        term = input("Enter search term: ")
        found = False
        for warehouse in stock_loader:  # Iterate through loaded stock warehouses
            results = warehouse.search(term)
            if results:
                print(f"Found in Warehouse {warehouse.id}:")
                for item in results:
                    print(item)
                actions.append(f"Searched for '{term}' in Warehouse {warehouse.id}.")
                found = True
        if not found:
            print("No items found matching your search.")
    elif command == "exit":
        break

# Say goodbye to the user
user.bye()
