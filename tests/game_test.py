import unittest
from src.Entity.Game import *

class game_test(unittest.TestCase):

    def test_create_new_game_instance_of_game(self):
        game = Game()
        self.assertIsInstance(game, Game)
    
    def test_new_game_frames_count_zero(self):
        game = Game()
        self.assertEquals(0, game.framesCount())
    
    def test_game_frame_count_for_one_roll_in_current_frame(self):
        game = Game()
        frame = game.roll(5)
        self.assertEquals(frame.getRollsLength(), 1)
    
    def test_game_after_two_rolls_current_frame_count_one(self):
        game = Game()
        game.roll(4)
        game.roll(5)
        self.assertEquals(1, game.framesCount())
    
    def test_game_four_rolls_result_two_frames(self):
        game = Game()
        game.roll(2)
        game.roll(5)
        game.roll(7)
        game.roll(2)
        self.assertEquals(2, game.framesCount())
    
    def test_game_six_rolls_result_three_frame(self):
        game = Game()
        game.roll(2)
        game.roll(5)
        game.roll(7)
        game.roll(2)
        game.roll(6)
        game.roll(2)
        self.assertEquals(3, game.framesCount())
    
    def test_game_score_one_roll(self):
        game = Game()
        game.roll(5)
        game.roll(3)
        self.assertEquals(8, game.score())