from src.Entity.Frame import *

class Game:
    def __init__(self):
        self.frames = {}
        self.frame_index = 1
        self.currentFrame = Frame()
    
    def framesCount(self):
        return self.frames.__len__()

    def roll(self, pins: int):
        self.currentFrame.roll(pins)
        if self.currentFrame.isFilled() == True :
            self.frames[self.frame_index] = self.currentFrame
            self.currentFrame = Frame()
            self.frame_index = self.frame_index + 1
            
        return self.currentFrame
    
    def score(self):
        score = 0
        for key, frame in self.frames.items() :
            score = score + frame.score()
        return score