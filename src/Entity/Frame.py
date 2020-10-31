from src.Entity.Roll import *

class Frame:
    
    def __init__(self):
        self.roll_index = 1
        self.rolls = {}
    
    def roll(self, pins: int):
        roll = Roll(pins)
        self.rolls[self.roll_index] = roll
        self.roll_index = self.roll_index + 1
        return roll