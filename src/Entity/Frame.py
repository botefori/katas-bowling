from src.Entity.Roll import *

class Frame:
    
    STRIKE_MAX_ROLLS = 1
    SPARE_MAX_ROLLS = 2
    CLASSIC_MAX_ROLLS = 1
    ROLL_MAX_PINS = 10
    
    def __init__(self):
        self.roll_index = 1
        self.rolls = {}
        self.is_strike = False
        self.is_spare = False
        self.is_classic = False
    
    def roll(self, pins: int):
        if self.getRollsLength() > 2 :
            raise Exception('Frame no more than three roll exception')
        roll = Roll(pins)
        self.rolls[self.roll_index] = roll
        self.roll_index = self.roll_index+1
    
        if self.getRollsLength() == 2 and self.score() < self.ROLL_MAX_PINS:
            self.is_classic = True
        if self.getRollsLength() == 2 and self.score() == self.ROLL_MAX_PINS:
            self.is_spare = True
        if self.getRollsLength() == 1 and pins == self.ROLL_MAX_PINS:
            self.is_strike = True
        return roll
    
    def score(self):
        score = 0
        for key, roll in self.rolls.items():
            score = score + roll.getPins()
        return score
    
    def isClassic(self):
       return self.is_classic
    
    def isSpare(self):
        return self.is_spare
    
    def isStrike(self):
        return self.is_strike
    
    def isFilled(self):
        if self.getRollsLength() > self.CLASSIC_MAX_ROLLS and self.isClassic():
            return True
        if self.getRollsLength() > self.SPARE_MAX_ROLLS and self.isSpare():
            return True
        if self.getRollsLength() > self.STRIKE_MAX_ROLLS and self.isStrike():
            return True
        return False
    
    def getRollsLength(self):
        return self.rolls.__len__()