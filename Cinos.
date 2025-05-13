class Drink:
    # Private class-level dictionaries for valid options and their prices
    __valid_bases = {
        "water": 1.00,
        "sbrite": 1.50,
        "pokecola": 1.75,
        "Mr.Salt": 2.00,
        "hill fog": 2.25,
        "leaf wine": 2.50
    }
    __valid_flavors = {
        "lemon": 0.15,
        "cherry": 0.15,
        "strawberry": 0.15,
        "mint": 0.15,
        "blueberry": 0.15,
        "lime": 0.15
    }
    __valid_sizes = {
        "small": 1.50,
        "medium": 1.75,
        "large": 2.05,
        "Mega": 2.15
    }
    __valid_food = {
        "hotdog": 2.30,
        "corndog": 2.00,
        "ice cream": 3.00,
        "onion rings": 1.75,
        "french fries": 1.50,
        "tater tots": 1.70,
        "nacho chips": 1.90
    }
    __valid_toppings = {
        "Cherry": 0.00,
        "Whipped Cream": 0.00,
        "Caramel Sauce": 0.50,
        "Chocolate Sauce": 0.50,
        "Nacho Cheese": 0.30,
        "Chilli": 0.60,
        "Bacon Bits": 0.30,
        "Ketchup": 0.00,
        "Mustard": 0.00
    }

    TAX_RATE = 0.0725  # 7.25% tax rate for all purchases

    def __init__(self):
        # Initialize instance variables to store selected options
        self.__base = None
        self.__flavor = set()
        self.__size = None
        self.__food = None
        self.__toppings = set()

    # Setter for base
    def set_base(self, base):
        if base in self.__valid_bases:
            self.__base = base
        else:
            raise ValueError(f"Invalid base: {base}.")

    # Add a flavor (can add multiple)
    def add_flavor(self, flavor):
        if flavor in self.__valid_flavors:
            self.__flavor.add(flavor)
        else:
            raise ValueError(f"Invalid flavor: {flavor}.")

    # Set the drink size
    def add_size(self, size):
        if size in self.__valid_sizes:
            self.__size = size
        else:
            raise ValueError(f"Invalid size: {size}.")

    # Add a food item
    def add_food(self, food):
        if food in self.__valid_food:
            self.__food = food
        else:
            raise ValueError(f"Invalid food: {food}.")

    # Add a topping (can add multiple)
    def add_topping(self, topping):
        if topping in self.__valid_toppings:
            self.__toppings.add(topping)
        else:
            raise ValueError(f"Invalid topping: {topping}.")

    # Getters for base, flavors, and size
    def get_base(self):
        return self.__base

    def get_flavors(self):
        return list(self.__flavor)

    def get_size(self):
        return self.__size

    # Calculate the total cost with tax
    def get_cost(self):
        cost = 0
        if self.__base:
            cost += self.__valid_bases[self.__base]
        for f in self.__flavor:
            cost += self.__valid_flavors[f]
        if self.__size:
            cost += self.__valid_sizes[self.__size]
        if self.__food:
            cost += self.__valid_food[self.__food]
        for topping in self.__toppings:
            cost += self.__valid_toppings[topping]
        tax = cost * self.TAX_RATE
        return round(cost + tax, 2)

    # Generate a formatted receipt as a string
    def generate_receipt(self):
        lines = ["======= DRINK RECEIPT ======="]
        lines.append(f"Base: {self.__base} - ${self.__valid_bases[self.__base]:.2f}" if self.__base else "Base: None")

        if self.__flavor:
            lines.append("Flavors:")
            for f in self.__flavor:
                lines.append(f"  - {f} - ${self.__valid_flavors[f]:.2f}")
        else:
            lines.append("Flavors: None")

        lines.append(f"Size: {self.__size} - ${self.__valid_sizes[self.__size]:.2f}" if self.__size else "Size: None")
        lines.append(f"Food: {self.__food} - ${self.__valid_food[self.__food]:.2f}" if self.__food else "Food: None")

        if self.__toppings:
            lines.append("Toppings:")
            for t in self.__toppings:
                lines.append(f"  - {t} - ${self.__valid_toppings[t]:.2f}")
        else:
            lines.append("Toppings: None")

        lines.append("=============================")
        subtotal = self.get_cost() / (1 + self.TAX_RATE)
        tax = subtotal * self.TAX_RATE
        lines.append(f"Subtotal: ${subtotal:.2f}")
        lines.append(f"Tax (7.25%): ${tax:.2f}")
        lines.append(f"Total (with tax): ${self.get_cost():.2f}")
        lines.append("=============================")
        return "\n".join(lines)

    # String representation of the drink (short summary)
    def __str__(self):
        if self.__base is None:
            return "Drink has no base."
        summary = f"Drink with base: {self.__base}"
        if self.__flavor:
            summary += f", flavors: {', '.join(self.__flavor)}"
        if self.__size:
            summary += f", size: {self.__size}"
        return summary + f". Total (with tax): ${self.get_cost():.2f}"

    # Debug representation for developer use
    def __repr__(self):
        return f"Drink(base={self.__base}, flavors={list(self.__flavor)}, size={self.__size}, total={self.get_cost():.2f})"


# Main function to interact with user
def main():
    drink = Drink()

    # Choose base
    print("Choose a base:")
    for idx, (base, price) in enumerate(Drink._Drink__valid_bases.items(), 1):
        print(f"{idx}. {base} - ${price:.2f}")
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            base_choice = list(Drink._Drink__valid_bases.keys())[choice - 1]
            drink.set_base(base_choice)
            print(f"Base '{base_choice}' selected!\n")
            break
        except (IndexError, ValueError):
            print("Invalid selection. Try again.")

    # Choose flavors
    print("Choose flavors (type 'done' to finish):")
    for idx, (flavor, price) in enumerate(Drink._Drink__valid_flavors.items(), 1):
        print(f"{idx}. {flavor} - ${price:.2f}")
    while True:
        choice = input("Enter flavor number or 'done': ").strip().lower()
        if choice == 'done':
            break
        try:
            flavor_index = int(choice)
            flavor = list(Drink._Drink__valid_flavors.keys())[flavor_index - 1]
            drink.add_flavor(flavor)
            print(f"Added flavor: {flavor}")
        except (IndexError, ValueError):
            print("Invalid choice. Try again.")

    # Choose size
    print("Choose a size:")
    for idx, (size, price) in enumerate(Drink._Drink__valid_sizes.items(), 1):
        print(f"{idx}. {size} - ${price:.2f}")
    while True:
        try:
            size_choice = int(input("Enter size number: "))
            size = list(Drink._Drink__valid_sizes.keys())[size_choice - 1]
            drink.add_size(size)
            print(f"Size '{size}' selected!\n")
            break
        except (IndexError, ValueError):
            print("Invalid selection. Try again.")

    # Choose food
    print("Choose a food item:")
    for idx, (food, price) in enumerate(Drink._Drink__valid_food.items(), 1):
        print(f"{idx}. {food} - ${price:.2f}")
    while True:
        try:
            food_choice = int(input("Enter food number: "))
            food = list(Drink._Drink__valid_food.keys())[food_choice - 1]
            drink.add_food(food)
            print(f"Food '{food}' selected!\n")
            break
        except (IndexError, ValueError):
            print("Invalid selection. Try again.")

    # Choose toppings
    print("Choose toppings (type 'done' to finish):")
    for idx, (topping, price) in enumerate(Drink._Drink__valid_toppings.items(), 1):
        print(f"{idx}. {topping} - ${price:.2f}")
    while True:
        choice = input("Enter topping number or 'done': ").strip().lower()
        if choice == 'done':
            break
        try:
            topping_index = int(choice)
            topping = list(Drink._Drink__valid_toppings.keys())[topping_index - 1]
            drink.add_topping(topping)
            print(f"Added topping: {topping}")
        except (IndexError, ValueError):
            print("Invalid choice. Try again.")

    # Output summary and receipt
    print("\nYour drink summary:")
    print(drink)

    print("\nReceipt:")
    print(drink.generate_receipt())


# Run the main function if the script is executed
if __name__ == "__main__":
    main()
