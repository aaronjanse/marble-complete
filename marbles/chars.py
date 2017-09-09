from .constants import LEFT_TILT, RIGHT_TILT

class Char(object):
    def __init__(self, env, pos, literal):
        self.env = env
        self.pos = pos
        self.literal = str(literal)

    def __str__(self):
        return self.literal

    def isMarble(self):
        return False

    def isToggler(self):
        return False


class MarbleChar(Char):
    def isMarble(self):
        return True


class Toggler(Char):
    def __init__(self, env, pos, literal):
        super().__init__(env, pos, literal)

        literal = str(literal)

        self.is_ascii = literal in 'tT'

        if literal in 't↘':
            self.tilt = LEFT_TILT
        elif literal in 'T↙':
            self.tilt = RIGHT_TILT
        else:
            raise Exception('invalid toggler char `{}`'.format(literal))

    def toggle(self):
        self.tilt = LEFT_TILT if self.tilt == RIGHT_TILT else RIGHT_TILT

    def isToggler(self):
        return True
