import unittest
from src.Entity.Frame import *

class frame_test(unittest.TestCase):
    
    def test_create_new_frame(self):
        frame = Frame()
        self.assertIsInstance(frame, Frame)

    def test_run_roll(self):
        frame = Frame();
        roll = frame.roll(5)
        self.assertIsInstance(roll, Roll)
        self.assertEquals(5, roll.getPins())
        
    def test_frame_roll_index(self):
        frame = Frame();
        curerentIndex = frame.getRollsLength()
        Roll = frame.roll(3)
        self.assertEquals(curerentIndex+1, frame.getRollsLength())
    
    def test_no_more_than_three_rolls_exception(self):
        frame = Frame()
        frame.roll(4)
        frame.roll(3)
        frame.roll(5)
        self.assertRaises(Exception, frame.roll, 4)