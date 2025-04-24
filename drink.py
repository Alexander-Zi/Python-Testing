class Drink:
    __valid_bases = {
        "water": 1.00,
        "sbrite": 1.50,
        "pokecola": 1.75,
        "Mr.Salt": 2.00,
        "hill fog": 2.25,
        "leaf wine": 2.50
    }

    __valid_flavors = {
        "lemon": 0.25,
        "cherry": 0.30,
        "strawberry": 0.35,
        "mint": 0.20,
        "blueberry": 0.40,
        "lime": 0.30
    }

    def __init__(self):
        self.__base = None
        self.__flavor = set()

    def set_base(self, base):
        if base in self.__valid_bases:
            self.__base = base
        else:
            raise ValueError(f"Invalid base: {base}. Valid bases are: {list(self.__valid_bases.keys())}")

    def add_flavor(self, flavor):
        if flavor in self.__valid_flavors:
            self.__flavor.add(flavor)
        else:
            raise ValueError(f"Invalid flavor: {flavor}. Valid flavors are: {list(self.__valid_flavors.keys())}")

    def get_base(self):
        return self.__base

    def get_flavors(self):
        return list(self.__flavor)

    def get_cost(self):
        cost = 0
        if self.__base:
            cost += self.__valid_bases[self.__base]
        for f in self.__flavor:
            cost += self.__valid_flavors[f]
        return round(cost, 2)

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

        lines.append(f"Total: ${self.get_cost():.2f}")
        lines.append("=============================")
        return "\n".join(lines)

    def __str__(self):
        if self.__base is None:
            return "Drink has no base."
        if not self.__flavor:
            return f"Drink with base: {self.__base} (${self.__valid_bases[self.__base]:.2f}) and no flavors. Total: ${self.get_cost():.2f}"
        flavor_list = ', '.join(self.__flavor)
        return (f"Drink with base: {self.__base} (${self.__valid_bases[self.__base]:.2f}) "
                f"and flavors: {flavor_list}. Total: ${self.get_cost():.2f}")

    def __repr__(self):
        return f"Drink(base={self.__base}, flavors={list(self.__flavor)}, total=${self.get_cost():.2f})"

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

    # Show final drink
    print("\n Your drink summary:")
    print(drink)

    # Show receipt
    print("\n Receipt:")
    print(drink.generate_receipt())


if __name__ == "__main__":
    main()
