from .constants import LEFT, RIGHT, UP, DOWN, LEFT_TILT, RIGHT_TILT

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

    def isGate(self):
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

    def send_pulse_over_wire(self, pos, known_positions=None):
        known_positions = known_positions or []

        if pos not in known_positions:
            known_positions.append(pos)
        else:
            return known_positions

        for direction in (LEFT, RIGHT, UP, DOWN):
            new_pos = pos + direction
            if not self.env.world.does_loc_exist(new_pos):
                continue

            if new_pos in known_positions:
                continue

            char = self.env.world.get_char_at(new_pos)
            if char.literal in '.+/\\┼╭╮╰╯┄┆':
                known_positions = self.send_pulse_over_wire(new_pos, known_positions)
            elif char.isToggler() or char.isGate():
                char.toggle()
                known_positions.append(new_pos)


        return known_positions

    def isToggler(self):
        return True

class Gate(Char):
    def __init__(self, env, pos, literal):
        super().__init__(env, pos, literal)

        literal = str(literal)

        if literal == ':':
            self.is_open = True
        elif literal == '!':
            self.is_open = False
        else:
            raise Exception('invalid toggler char `{}`'.format(literal))

    def toggle(self):
        self.is_open = not self.is_open

    def isGate(self):
        return True
