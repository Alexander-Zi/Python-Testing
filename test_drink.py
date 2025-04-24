import unittest
from unittest.mock import patch
from io import StringIO
from drink import Drink, main


class TestDrinkClass(unittest.TestCase):

    def test_valid_base(self):
        d = Drink()
        d.set_base("sbrite")
        self.assertEqual(d.get_base(), "sbrite")

    def test_invalid_base(self):
        d = Drink()
        with self.assertRaises(ValueError):
            d.set_base("lava")

    def test_add_valid_flavor(self):
        d = Drink()
        d.add_flavor("cherry")
        self.assertIn("cherry", d.get_flavors())

    def test_add_invalid_flavor(self):
        d = Drink()
        with self.assertRaises(ValueError):
            d.add_flavor("coconut")

    def test_cost_calculation(self):
        d = Drink()
        d.set_base("pokecola")  
        d.add_flavor("lemon")   
        d.add_flavor("lime")    
        self.assertEqual(d.get_cost(), 2.30)

    def test_str_with_base_no_flavors(self):
        d = Drink()
        d.set_base("hill fog")
        self.assertIn("no flavors", str(d))

    def test_str_with_flavors(self):
        d = Drink()
        d.set_base("Mr.Salt")
        d.add_flavor("mint")
        out = str(d)
        self.assertIn("Mr.Salt", out)
        self.assertIn("mint", out)
        self.assertIn("Total", out)

    def test_receipt_format(self):
        d = Drink()
        d.set_base("leaf wine")
        d.add_flavor("blueberry")
        receipt = d.generate_receipt()
        self.assertIn("leaf wine", receipt)
        self.assertIn("blueberry", receipt)
        self.assertIn("Total", receipt)
        self.assertTrue(receipt.startswith("======= DRINK RECEIPT ======="))

    def test_no_base_output(self):
        d = Drink()
        self.assertEqual(str(d), "Drink has no base.")


class TestDrinkMain(unittest.TestCase):

    @patch('builtins.input', side_effect=[
        '2',       
        '1',        
        '2',        
        'done'     
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_program_output(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Base 'sbrite' selected", output)
        self.assertIn("Added flavor: lemon", output)
        self.assertIn("Added flavor: cherry", output)
        self.assertIn("DRINK RECEIPT", output)
        self.assertIn("Total: $2.05", output)  


if __name__ == '__main__':
    unittest.main()
