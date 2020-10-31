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
        curerentIndex = frame.roll_index
        Roll = frame.roll(3)
        self.assertEquals(curerentIndex+1, frame.roll_index)