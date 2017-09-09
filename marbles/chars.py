from .constants import LEFT_TILT, RIGHT_TILT

class Char(str):
    def __init__(self, value):
        self.value = value

    def isMarble(self):
        return False

    def isToggler(self):
        return False


class MarbleChar(Char):
    def isMarble(self):
        return True


class Toggler(Char):
    def __init__(self, value):
        super().__init__(value)

        self.is_ascii = value in 'tT'

        if value in 't↘':
            self.tilt = LEFT_TILT
        elif value in 'T↙':
            self.tilt = RIGHT_TILT
        else:
            raise Exception('invalid toggler char `{}`'.format(value))

    def toggle(self):
        self.tilt = LEFT_TILT if self.tilt == RIGHT_TILT else RIGHT_TILT

    def isToggler(self):
        return True
