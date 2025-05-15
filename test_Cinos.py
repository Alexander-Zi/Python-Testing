from unittest.mock import patch
import unittest
from io import StringIO
from Cinos import Drink, main


class TestDrink(unittest.TestCase):

    def test_set_and_get_base(self):
        d = Drink()
        d.set_base("pokecola")
        self.assertEqual(d.get_base(), "pokecola")

    def test_invalid_base_raises(self):
        d = Drink()
        with self.assertRaises(ValueError):
            d.set_base("lava juice")

    def test_add_flavor_and_get_flavors(self):
        d = Drink()
        d.add_flavor("lemon")
        d.add_flavor("cherry")
        self.assertIn("lemon", d.get_flavors())
        self.assertIn("cherry", d.get_flavors())

    def test_invalid_flavor_raises(self):
        d = Drink()
        with self.assertRaises(ValueError):
            d.add_flavor("bubblegum")

    def test_set_and_get_size(self):
        d = Drink()
        d.add_size("medium")
        self.assertEqual(d.get_size(), "medium")

    def test_invalid_size_raises(self):
        d = Drink()
        with self.assertRaises(ValueError):
            d.add_size("extra grande")

    def test_add_food_and_cost(self):
        d = Drink()
        d.set_base("water")
        d.add_flavor("lemon")
        d.add_size("small")
        d.add_food("hotdog")
        subtotal = 1.00 + 0.15 + 1.50 + 2.30
        expected = round(subtotal * 1.0725, 2)
        self.assertEqual(d.get_cost(), expected)

    def test_invalid_food_raises(self):
        d = Drink()
        with self.assertRaises(ValueError):
            d.add_food("lava fries")

    def test_add_toppings_and_cost(self):
        d = Drink()
        d.set_base("water")
        d.add_flavor("lemon")
        d.add_size("small")
        d.add_food("hotdog")
        d.add_topping("Ketchup")
        d.add_topping("Chilli")
        subtotal = 1.00 + 0.15 + 1.50 + 2.30 + 0.00 + 0.60
        expected = round(subtotal * 1.0725, 2)
        self.assertEqual(d.get_cost(), expected)

    def test_invalid_topping_raises(self):
        d = Drink()
        with self.assertRaises(ValueError):
            d.add_topping("gold flakes")

    def test_add_icecream_and_cost(self):
        d = Drink()
        d.set_base("pokecola")
        d.add_size("Mega")
        d.set_icecream_flavor("S'more")
        d.add_icecream_topping("Cookie Dough")
        d.add_icecream_topping("Pecans")
        subtotal = 1.75 + 2.15 + 4.00 + 1.00 + 0.50
        expected = round(subtotal * 1.0725, 2)
        self.assertEqual(d.get_cost(), expected)

    def test_invalid_icecream_flavor_raises(self):
        d = Drink()
        with self.assertRaises(ValueError):
            d.set_icecream_flavor("rainbow")

    def test_invalid_icecream_topping_raises(self):
        d = Drink()
        with self.assertRaises(ValueError):
            d.add_icecream_topping("sprinkles")

    def test_generate_receipt_contains_all(self):
        d = Drink()
        d.set_base("pokecola")
        d.add_flavor("lime")
        d.add_size("Mega")
        d.add_food("ice cream")
        d.add_topping("Chilli")
        d.set_icecream_flavor("Chocolate")
        d.add_icecream_topping("Cookie Dough")
        receipt = d.generate_receipt()
        self.assertIn("Base: pokecola", receipt)
        self.assertIn("Flavors:", receipt)
        self.assertIn("Size: Mega", receipt)
        self.assertIn("Food: ice cream", receipt)
        self.assertIn("Toppings:", receipt)
        self.assertIn("Ice Cream: Chocolate", receipt)
        self.assertIn("Ice Cream Toppings:", receipt)

    def test_str_representation_with_icecream(self):
        d = Drink()
        d.set_base("hill fog")
        d.add_flavor("blueberry")
        d.add_size("large")
        d.set_icecream_flavor("Vanilla Bean")
        result = str(d)
        self.assertIn("hill fog", result)
        self.assertIn("blueberry", result)
        self.assertIn("large", result)
        self.assertIn("Total (with tax):", result)

    def test_str_only_base(self):
        d = Drink()
        d.set_base("water")
        self.assertIn("Drink with base: water", str(d))

    def test_str_no_base(self):
        d = Drink()
        self.assertEqual(str(d), "Drink has no base.")


class TestMainIntegration(unittest.TestCase):

    @patch("builtins.input", side_effect=[
        '2',       # base: sbrite
        '1',       # flavor: lemon
        '2',       # flavor: cherry
        'done',    # done with flavors
        '1',       # size: small
        '1',       # food: hotdog
        '1',       # topping: Cherry
        '6',       # topping: Chilli
        'done',    # done with toppings
        '2',       # ice cream flavor: Chocolate
        '4',       # topping: Chocolate Sauce
        '8',       # topping: Cookie Dough
        'done'     # done with ice cream toppings
    ])
    @patch("sys.stdout", new_callable=StringIO)
    def test_main_output(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Drink with base: sbrite", output or "")
        self.assertIn("lemon", output or "")
        self.assertIn("cherry", output or "")
        self.assertIn("Food: hotdog - $2.30", output or "")
        self.assertIn("Cherry - $0.00", output or "")
        self.assertIn("Chilli - $0.60", output or "")
        self.assertIn("Ice Cream: Chocolate - $3.00", output or "")
        self.assertIn("Chocolate Sauce - $0.50", output or "")
        self.assertIn("Cookie Dough - $1.00", output or "")
        self.assertIn("DRINK RECEIPT", output or "")


if __name__ == "__main__":
    unittest.main()
