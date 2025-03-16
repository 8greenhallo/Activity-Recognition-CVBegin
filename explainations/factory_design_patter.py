from abc import ABC, abstractmethod

# Step 1: Define the Product interface
class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass

# Step 2: Implement Concrete Products
class Espresso(Coffee):
    def prepare(self):
        return "Preparing a rich and strong Espresso."

class Latte(Coffee):
    def prepare(self):
        return "Preparing a smooth and creamy Latte."

class Cappuccino(Coffee):
    def prepare(self):
        return "Preparing a frothy Cappuccino."

# Step 3: Implement the Factory [CoffeeMachine]
class CoffeeMachine:
    def make_coffee(self, coffee_type) -> String:
        if coffee_type == "Espresso":
            return Espresso().prepare()
        elif coffee_type == "Latte":
            return Latte().prepare()
        elif coffee_type == "Cappuccino":
            return Cappuccino().prepare()
        else:
            return "Unknown coffee type!"

# Step 4: Use the Factory to Create Product
if __name__ == "__main__":
    machine = CoffeeMachine()

    ctype = ["Espresso", "Latte", "Cappuccino"]

    for t in ctype:
        coffee = machine.make_coffee(t)
        print(coffee) # Output: preparing a rich and strong Espresso
