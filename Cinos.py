class Drink:
    # This class represents a drink with a base, flavors, and size. As well as the price.
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

    TAX_RATE = 0.0725  # 7.25% tax rate

    def __init__(self):
        self.__base = None
        self.__flavor = set()
        self.__size = None  # A single size, not a set

    #  This will be used to set the base   
    def set_base(self, base):
        if base in self.__valid_bases:
            self.__base = base
        else:
            raise ValueError(f"Invalid base: {base}. Valid bases are: {list(self.__valid_bases.keys())}")

# this will be used to add flavors
    def add_flavor(self, flavor):
        if flavor in self.__valid_flavors:
            self.__flavor.add(flavor)
        else:
            raise ValueError(f"Invalid flavor: {flavor}. Valid flavors are: {list(self.__valid_flavors.keys())}")
# This will be used to set the size       
    def add_size(self, size):
        if size in self.__valid_sizes:
            self.__size = size
        else:
            raise ValueError(f"Invalid size: {size}. Valid sizes are: {list(self.__valid_sizes.keys())}")

    def get_base(self):
        return self.__base

    def get_flavors(self):
        return list(self.__flavor)
    
    def get_size(self):
        return self.__size
    
    #This will be used to find the cost
    def get_cost(self):
        cost = 0
        if self.__base:
            cost += self.__valid_bases[self.__base]
        for f in self.__flavor:
            cost += self.__valid_flavors[f]
        if self.__size:
            cost += self.__valid_sizes[self.__size]
        
        tax = cost * self.TAX_RATE  # Calculate tax
        total_cost = cost + tax  # Add tax to the total cost
        return round(total_cost, 2)

#The receipt will be generated here
    def generate_receipt(self):
        lines = []
        lines.append("======= DRINK RECEIPT =======")
        if self.__base:
            base_cost = self.__valid_bases[self.__base]
            lines.append(f"Base: {self.__base} - ${base_cost:.2f}")
        else:
            lines.append("Base: None")

        if self.__flavor:
            lines.append("Flavors:")
            for f in self.__flavor:
                flavor_cost = self.__valid_flavors[f]
                lines.append(f"  - {f} - ${flavor_cost:.2f}")
        else:
            lines.append("Flavors: None")
        
        if self.__size:
            size_cost = self.__valid_sizes[self.__size]
            lines.append(f"Size: {self.__size} - ${size_cost:.2f}")
        else:
            lines.append("Size: None")

        cost_before_tax = self.get_cost() / (1 + self.TAX_RATE)  # Get the cost before tax
        tax = cost_before_tax * self.TAX_RATE  # Calculate the tax
        lines.append(f"Subtotal: ${cost_before_tax:.2f}")
        lines.append(f"Tax (7.25%): ${tax:.2f}")
        lines.append(f"Total (with tax): ${self.get_cost():.2f}")
        lines.append("=============================")
        return "\n".join(lines)
    
# The __str__ method will be used to print the drink object
    def __str__(self):
        if self.__base is None:
            return "Drink has no base."
        if not self.__flavor:
            return f"Drink with base: {self.__base} (${self.__valid_bases[self.__base]:.2f}) and no flavors. Total (with tax): ${self.get_cost():.2f}"
        flavor_list = ', '.join(self.__flavor)
        if not self.__size:
            return (f"Drink with base: {self.__base} (${self.__valid_bases[self.__base]:.2f}) "
                    f"and flavors: {flavor_list}. Total (with tax): ${self.get_cost():.2f}")
        return (f"Drink with base: {self.__base} (${self.__valid_bases[self.__base]:.2f}) "
                f"and flavors: {flavor_list} and size: {self.__size}. Total (with tax): ${self.get_cost():.2f}")

    def __repr__(self):
        return f"Drink(base={self.__base}, flavors={list(self.__flavor)}, size={self.__size}, total={self.get_cost():.2f})"


# The main function will be used to interact with the user
def main():
    drink = Drink()

    # Choose base
    print("Choose a base from the following options:")
    for idx, (base, price) in enumerate(Drink._Drink__valid_bases.items(), 1):
        print(f"{idx}. {base} - ${price:.2f}")
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            base_choice = list(Drink._Drink__valid_bases.keys())[choice - 1]
            drink.set_base(base_choice)
            print(f"\n Base '{base_choice}' selected!\n")
            break
        except (IndexError, ValueError):
            print(" Invalid selection. Please choose a valid number.\n")

    # Choose flavors
    print("Now choose flavors (enter the number, type 'done' to finish):")
    for idx, (flavor, price) in enumerate(Drink._Drink__valid_flavors.items(), 1):
        print(f"{idx}. {flavor} - ${price:.2f}")
        
#   Allow multiple flavors to be added
    while True:
        user_input = input("Enter flavor number or 'done': ").strip().lower()
        if user_input == 'done':
            break
        try:
            flavor_index = int(user_input)
            flavor_choice = list(Drink._Drink__valid_flavors.keys())[flavor_index - 1]
            drink.add_flavor(flavor_choice)
            print(f" Added flavor: {flavor_choice}")
        except (IndexError, ValueError):
            print(" Invalid choice. Try again.")

    # Choose size
    print("Now choose a size:")
    for idx, (size, price) in enumerate(Drink._Drink__valid_sizes.items(), 1):
        print(f"{idx}. {size} - ${price:.2f}")

#  Allow only one size to be added
    while True:
        try:
            size_choice = int(input("Enter the number of your choice: "))
            size = list(Drink._Drink__valid_sizes.keys())[size_choice - 1]
            drink.add_size(size)
            print(f"\n Size '{size}' selected!\n")
            break
        except (IndexError, ValueError):
            print(" Invalid selection. Please choose a valid number.\n")

    # Show final drink
    print("\n Your drink summary:")
    print(drink)

    # Show receipt
    print("\n Receipt:")
    print(drink.generate_receipt())


if __name__ == "__main__":
    main()