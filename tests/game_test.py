import unittest
from src.Entity.Game import *

class game_test(unittest.TestCase):

    def test_create_new_game_instance_of_game(self):
        game = Game()
        self.assertIsInstance(game, Game)
    
    def test_new_game_frames_count_zero(self):
        game = Game()
        self.assertEquals(0, game.framesCount())