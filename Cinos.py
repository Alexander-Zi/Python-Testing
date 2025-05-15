class Drink:
    # Class-level private dictionaries storing valid options and their prices
    __valid_bases = {  # Drink base options
        "water": 1.00,
        "sbrite": 1.50,
        "pokecola": 1.75,
        "Mr.Salt": 2.00,
        "hill fog": 2.25,
        "leaf wine": 2.50
    }
    __valid_flavors = {  # Drink flavor options
        "lemon": 0.15,
        "cherry": 0.15,
        "strawberry": 0.15,
        "mint": 0.15,
        "blueberry": 0.15,
        "lime": 0.15
    }
    __valid_sizes = {  # Drink size options
        "small": 1.50,
        "medium": 1.75,
        "large": 2.05,
        "Mega": 2.15
    }
    __valid_food = {  # Side food options
        "hotdog": 2.30,
        "corndog": 2.00,
        "ice cream": 3.00,
        "onion rings": 1.75,
        "french fries": 1.50,
        "tater tots": 1.70,
        "nacho chips": 1.90
    }
    __valid_toppings = {  # Drink topping options
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
    __valid_icecream_flavor = {  # Ice cream flavor options
        "Mint Chocolate Chip": 4.00,
        "Chocolate": 3.00,
        "Vanilla Bean": 3.00,
        "Banana": 3.50,
        "Butter Pecan": 3.50,
        "S'more": 4.00
    }
    __valid_icecreamtoppings = {  # Ice cream toppings
        "Cherry": 0.00,
        "Whipped Cream": 0.00,
        "Caramel Sauce": 0.50,
        "Chocolate Sauce": 0.50,
        "Storios": 1.00,
        "Dig Dogs": 1.00,
        "T&T's": 1.00,
        "Cookie Dough": 1.00,
        "Pecans": 0.50,
    }

    TAX_RATE = 0.0725  # Constant tax rate of 7.25%

    def __init__(self):
        # Instance variables to store customer selections
        self.__base = None
        self.__flavor = set()
        self.__size = None
        self.__food = None
        self.__toppings = set()
        self.__icecream_flavor = None
        self.__icecream_toppings = set()

    # Setter methods with validation
    def set_base(self, base):
        if base in self.__valid_bases:
            self.__base = base
        else:
            raise ValueError(f"Invalid base: {base}.")

    def add_flavor(self, flavor):
        if flavor in self.__valid_flavors:
            self.__flavor.add(flavor)
        else:
            raise ValueError(f"Invalid flavor: {flavor}.")

    def add_size(self, size):
        if size in self.__valid_sizes:
            self.__size = size
        else:
            raise ValueError(f"Invalid size: {size}.")

    def add_food(self, food):
        if food in self.__valid_food:
            self.__food = food
        else:
            raise ValueError(f"Invalid food: {food}.")

    def add_topping(self, topping):
        if topping in self.__valid_toppings:
            self.__toppings.add(topping)
        else:
            raise ValueError(f"Invalid topping: {topping}.")

    def set_icecream_flavor(self, flavor):
        if flavor in self.__valid_icecream_flavor:
            self.__icecream_flavor = flavor
        else:
            raise ValueError(f"Invalid ice cream flavor: {flavor}.")

    def add_icecream_topping(self, topping):
        if topping in self.__valid_icecreamtoppings:
            self.__icecream_toppings.add(topping)
        else:
            raise ValueError(f"Invalid ice cream topping: {topping}.")

    # Getter methods
    def get_base(self):
        return self.__base

    def get_flavors(self):
        return list(self.__flavor)

    def get_size(self):
        return self.__size

    # Cost calculation including all selected items and tax
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
        if self.__icecream_flavor:
            cost += self.__valid_icecream_flavor[self.__icecream_flavor]
        for t in self.__icecream_toppings:
            cost += self.__valid_icecreamtoppings[t]
        tax = cost * self.TAX_RATE
        return round(cost + tax, 2)

    # Prints a formatted receipt of the full order
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

        if self.__icecream_flavor:
            lines.append(f"Ice Cream: {self.__icecream_flavor} - ${self.__valid_icecream_flavor[self.__icecream_flavor]:.2f}")
        else:
            lines.append("Ice Cream: None")

        if self.__icecream_toppings:
            lines.append("Ice Cream Toppings:")
            for t in self.__icecream_toppings:
                lines.append(f"  - {t} - ${self.__valid_icecreamtoppings[t]:.2f}")
        else:
            lines.append("Ice Cream Toppings: None")

        lines.append("=============================")
        subtotal = self.get_cost() / (1 + self.TAX_RATE)
        tax = subtotal * self.TAX_RATE
        lines.append(f"Subtotal: ${subtotal:.2f}")
        lines.append(f"Tax (7.25%): ${tax:.2f}")
        lines.append(f"Total (with tax): ${self.get_cost():.2f}")
        lines.append("=============================")
        return "\n".join(lines)

    def __str__(self):
        # Friendly string representation for print()
        if self.__base is None:
            return "Drink has no base."
        summary = f"Drink with base: {self.__base}"
        if self.__flavor:
            summary += f", flavors: {', '.join(self.__flavor)}"
        if self.__size:
            summary += f", size: {self.__size}"
        return summary + f". Total (with tax): ${self.get_cost():.2f}"

    def __repr__(self):
        # Debug-style representation
        return f"Drink(base={self.__base}, flavors={list(self.__flavor)}, size={self.__size}, total={self.get_cost():.2f})"


def main():
    # Main interaction loop
    drink = Drink()

    # Base selection
    print("Choose a base:")
    for idx, (base, price) in enumerate(Drink._Drink__valid_bases.items(), 1):
        print(f"{idx}. {base} - ${price:.2f}")
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            base_choice = list(Drink._Drink__valid_bases.keys())[choice - 1]
            drink.set_base(base_choice)
            break
        except (IndexError, ValueError):
            print("Invalid selection. Try again.")

    # Flavor selection loop
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
        except (IndexError, ValueError):
            print("Invalid choice. Try again.")

    # Size selection
    print("Choose a size:")
    for idx, (size, price) in enumerate(Drink._Drink__valid_sizes.items(), 1):
        print(f"{idx}. {size} - ${price:.2f}")
    while True:
        try:
            size_choice = int(input("Enter size number: "))
            size = list(Drink._Drink__valid_sizes.keys())[size_choice - 1]
            drink.add_size(size)
            break
        except (IndexError, ValueError):
            print("Invalid selection. Try again.")

    # Food selection
    print("Choose a food item:")
    for idx, (food, price) in enumerate(Drink._Drink__valid_food.items(), 1):
        print(f"{idx}. {food} - ${price:.2f}")
    while True:
        try:
            food_choice = int(input("Enter food number: "))
            food = list(Drink._Drink__valid_food.keys())[food_choice - 1]
            drink.add_food(food)
            break
        except (IndexError, ValueError):
            print("Invalid selection. Try again.")

    # Toppings selection
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
        except (IndexError, ValueError):
            print("Invalid choice. Try again.")

    # Ice cream flavor selection
    print("Choose an ice cream flavor:")
    for idx, (flavor, price) in enumerate(Drink._Drink__valid_icecream_flavor.items(), 1):
        print(f"{idx}. {flavor} - ${price:.2f}")
    while True:
        choice = input("Enter flavor number or 'none': ").strip().lower()
        if choice == 'none':
            break
        try:
            flavor_index = int(choice)
            flavor = list(Drink._Drink__valid_icecream_flavor.keys())[flavor_index - 1]
            drink.set_icecream_flavor(flavor)
            break
        except (IndexError, ValueError):
            print("Invalid selection. Try again.")

    # Ice cream toppings selection
    print("Choose ice cream toppings (type 'done' to finish):")
    for idx, (topping, price) in enumerate(Drink._Drink__valid_icecreamtoppings.items(), 1):
        print(f"{idx}. {topping} - ${price:.2f}")
    while True:
        choice = input("Enter topping number or 'done': ").strip().lower()
        if choice == 'done':
            break
        try:
            topping_index = int(choice)
            topping = list(Drink._Drink__valid_icecreamtoppings.keys())[topping_index - 1]
            drink.add_icecream_topping(topping)
        except (IndexError, ValueError):
            print("Invalid choice. Try again.")

    # Output final result
    print("\nYour drink summary:")
    print(drink)

    print("\nReceipt:")
    print(drink.generate_receipt())


if __name__ == "__main__":
    main()
