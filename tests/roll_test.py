import unittest
from src.Entity.Roll import *

class roll_test(unittest.TestCase):
    
    def test_set_pins_ok(self):
        roll = Roll(7)
        self.assertEquals(7, roll.getPins())
        
    def test_exception_bad_pins_value_type(self):
        self.assertRaises(Exception, Roll, 'iou')
    
    def test_exception_pins_bad_value(self):
        self.assertRaises(Exception, Roll, -1)