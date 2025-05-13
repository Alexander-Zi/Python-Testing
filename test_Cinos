import unittest
from Cinos import Drink
from unittest.mock import patch
from io import StringIO


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
        d.add_food("hotdog")
        d.set_base("water")
        d.add_size("small")
        subtotal = 1.00 + 1.50 + 2.30
        expected = round(subtotal * 1.0725, 2)
        self.assertEqual(d.get_cost(), expected)

    def test_invalid_food_raises(self):
        d = Drink()
        with self.assertRaises(ValueError):
            d.add_food("lava fries")

    def test_add_toppings_and_cost(self):
        d = Drink()
        d.set_base("water")
        d.add_size("small")
        d.add_food("hotdog")
        d.add_topping("Ketchup")
        d.add_topping("Chilli")
        subtotal = 1.00 + 1.50 + 2.30 + 0.00 + 0.60
        expected = round(subtotal * 1.0725, 2)
        self.assertEqual(d.get_cost(), expected)

    def test_invalid_topping_raises(self):
        d = Drink()
        with self.assertRaises(ValueError):
            d.add_topping("gold flakes")

    def test_generate_receipt_format(self):
        d = Drink()
        d.set_base("hill fog")
        d.add_flavor("blueberry")
        d.add_size("large")
        d.add_food("ice cream")
        d.add_topping("Cherry")
        receipt = d.generate_receipt()
        self.assertIn("======= DRINK RECEIPT =======", receipt)
        self.assertIn("Base: hill fog - $2.25", receipt)
        self.assertIn("- blueberry - $0.15", receipt)
        self.assertIn("Size: large - $2.05", receipt)
        self.assertIn("Food: ice cream - $3.00", receipt)
        self.assertIn("Toppings:", receipt)
        self.assertIn("- Cherry - $0.00", receipt)
        self.assertIn("Total (with tax):", receipt)

    def test_str_representation(self):
        d = Drink()
        d.set_base("leaf wine")
        d.add_flavor("mint")
        d.add_size("Mega")
        output = str(d)
        self.assertIn("leaf wine", output)
        self.assertIn("mint", output)
        self.assertIn("Mega", output)
        self.assertIn("Total (with tax):", output)

    def test_str_only_base(self):
        d = Drink()
        d.set_base("water")
        output = str(d)
        self.assertIn("Drink with base: water", output)

    def test_str_no_base(self):
        d = Drink()
        self.assertEqual(str(d), "Drink has no base.")


class TestMainIntegration(unittest.TestCase):

    @patch("builtins.input", side_effect=[
        '2',       # base: sbrite ($1.50)
        '1',       # flavor: lemon ($0.15)
        '2',       # flavor: cherry ($0.15)
        'done',
        '1',       # size: small ($1.50)
        '1',       # food: hotdog ($2.30)
        '1',       # topping: Cherry ($0.00)
        '6',       # topping: Chilli ($0.60)
        'done'
    ])
    @patch("sys.stdout", new_callable=StringIO)
    def test_main_output(self, mock_stdout, mock_input):
        from Cinos import main
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Base 'sbrite' selected", output)
        self.assertIn("Added flavor: lemon", output)
        self.assertIn("Added flavor: cherry", output)
        self.assertIn("Food 'hotdog' selected", output)
        self.assertIn("Added topping: Cherry", output)
        self.assertIn("Added topping: Chilli", output)
        self.assertIn("DRINK RECEIPT", output)

        subtotal = 1.50 + 0.15 + 0.15 + 1.50 + 2.30 + 0.00 + 0.60
        expected_total = round(subtotal * 1.0725, 2)
        self.assertIn(f"Total (with tax): ${expected_total:.2f}", output)


if __name__ == "__main__":
    unittest.main()
