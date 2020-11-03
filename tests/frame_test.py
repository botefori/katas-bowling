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
    
    def test_score_for_zero_roll(self):
        frame = Frame()
        self.assertEquals(0, frame.score())
    
    def test_score_for_one_roll(self):
        frame = Frame()
        frame.roll(4)
        self.assertEquals(4, frame.score())
    
    def test_score_for_two_roll(self):
        frame = Frame()
        frame.roll(4)
        frame.roll(5)
        self.assertEquals(9, frame.score())
    
    def test_score_for_three_rolls(self):
        frame = Frame()
        frame.roll(4)
        frame.roll(6)
        frame.roll(3)
        self.assertEquals(13, frame.score())
    
    def test_frame_is_classic(self):
        frame = Frame()
        frame.roll(2)
        frame.roll(5)
        self.assertTrue(frame.isClassic())
    
    def test_frame_is_spare(self):
        frame = Frame()
        frame.roll(6)
        frame.roll(4)
        self.assertTrue(frame.isSpare())
    
    def test_frame_is_strike(self):
        frame = Frame()
        frame.roll(10)
        self.assertTrue(frame.isStrike())
    
    def test_frame_is_filled_on_classic(self):
        frame = Frame()
        frame.roll(3)
        frame.roll(5)
        self.assertTrue(frame.isFilled())
    
    def test_frame_classic_not_filled(self):
        frame = Frame()
        frame.roll(7)
        self.assertFalse(frame.isFilled())
    
    def test_frame_is_filled_on_spare(self):
        frame = Frame()
        frame.roll(4)
        frame.roll(6)
        frame.roll(7)
        self.assertTrue(frame.isFilled())

    def test_frame_spare_not_filled(self):
        frame = Frame()
        frame.roll(7)
        frame.roll(3)
        self.assertFalse(frame.isFilled())

    def test_frame_is_filled_on_strike(self):
        frame = Frame()
        frame.roll(10)
        frame.roll(6)
        self.assertTrue(frame.isFilled())
    
    def test_frame_strike_is_not_filled(self):
        frame = Frame()
        frame.roll(10)
        self.assertFalse(frame.isFilled())