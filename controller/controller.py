from random import randint


class Dice:
    d1 = None
    d2 = None

    def roll(self, frame_hook, method):
        self.d1 = randint(1, 6)
        self.d2 = randint(1, 6)
        method(frame_hook, self)

