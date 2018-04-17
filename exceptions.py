class InvalidPlayerCountException(Exception):

    def __init__(self, message=None):
        if message is None:
            self.message = "Invalid Player count"
        else:
            self.message = message


class InvalidDockOrientation(Exception):

    def __init__(self, rotation, message=None):
        if message is None:
            self.message = "Rotation of dock must be multiple of 60 and must be in between 0 and 300, given: {}".format(
                rotation)
        else:
            self.message = message
