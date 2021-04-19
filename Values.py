
class Values:
    def __init__(self, c, neg, neu, pos):
        self.compound = c
        self.negative = neg
        self.neutral = neu
        self.positive = pos


    def __str__(self):
        return "Compund: " + str(self.compound) + " Neg: " + str(self.negative) +  " Neu: " + str(self.neutral) + " Pos: " + str(self.positive)

    def get_compound(self):
        return self.compound





