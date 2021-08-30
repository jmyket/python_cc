import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the 'Employee' class."""

    def setUp(self):
        """Create instance of 'Employee' class to test."""
        f = "Josh"
        l = "Myket"
        sal = 65_000
        self.my_emp = Employee(f, l, sal)
        self.p_inc = 12_000
    
    def test_give_default_raise(self):
        """Test that default value used in 'give_raise' works."""
        old_pay = self.my_emp.salary
        self.my_emp.give_raise()
        new_pay = self.my_emp.salary
        diff = new_pay - old_pay
        self.assertEqual(diff, 5000)

    def test_give_custom_raise(self):
        """Test that custom values used in 'give_raise' works."""
        old_pay = self.my_emp.salary
        self.my_emp.give_raise(self.p_inc)
        new_pay = self.my_emp.salary
        diff = new_pay - old_pay
        self.assertEqual(diff, self.p_inc)

if __name__ == "__main__":
    unittest.main()
        