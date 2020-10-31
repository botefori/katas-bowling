class Roll:
    
    def __init__(self, pins: int):
        if isinstance(pins, int) == False:
            raise Exception('pins argument must be int')
        if pins < 0 or pins > 10 :
            raise('pins value must be between 0 and 10')
        self.pins = pins
        
    def getPins(self):
        return self.pins