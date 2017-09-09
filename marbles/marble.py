import sys

from .constants import DIRECTIONS, RIGHT, LEFT, UP, DOWN, RIGHT_TILT
from .vector import Pos


class Marble:
    def __init__(self, env, pos, direction=None):
        """
        The base unit of and ascii marble code : the marble.

        :param marbles.environement.Env env: The environement for the program
        :param marbles.vector.Pos pos: The position of the marble in the map
        :param marbles.vector.Pos direction: The direction of the marble
        """

        self.pos = pos

        self.env = env
        self.dir = direction or self._calculate_direction()

        self.is_dead = False

    def __repr__(self):
        return '<Marble pos={pos}, dir={dir}>'.format(**self.__dict__)

    def simulate_tick(self):
        # If outside the map, he dies.
        if not self.env.world.does_loc_exist(self.pos):
            self.is_dead = True
            return

        char = self.env.world.get_char_at(self.pos)

        # end of execution
        if char == '&':
            self.is_dead = True

            self.env.io.on_finish()
            sys.exit(0)

        # update the marble's position
        self.move(char)

    def move(self, char):
        if char in '\\╗╚':
            self._change_dir_with_func(lambda dir: Pos(dir.y, dir.x))
        elif char in '/╝╔':
            self._change_dir_with_func(lambda dir: Pos(-dir.y, -dir.x))
        elif char == '(':
            self.dir = RIGHT
        elif char == ')':
            self.dir = LEFT
        elif char in '>⇒' and self._is_moving_vert():
            self.dir = RIGHT
        elif char in '<⇐' and self._is_moving_vert():
            self.dir = LEFT
        elif char in '^⇑' and self._is_moving_horiz():
            self.dir = UP
        elif char in 'v⇓' and self._is_moving_horiz():
            self.dir = DOWN
        elif char == '*':
            for dir in DIRECTIONS:
                if self.dir in (dir, -dir):
                    continue

                next_pos = self.pos + dir

                if self.env.world.does_loc_exist(next_pos) and self.env.world.get_char_at(next_pos) != ' ':
                    new_marble = Marble(self.env, self.pos, direction=dir)
                    new_marble.pos += dir # make sure it doesn't start on the astrisk and duplicate itself

                    self.env.marbles.append(new_marble)
        elif char.isToggler():
            self.dir = LEFT if char.tilt == RIGHT_TILT else RIGHT
            char.toggle()
        elif char == ' ':
            self.is_dead = True

        self.pos += self.dir

    def _is_moving_vert(self):
        """True if the marble is moving verticaly."""
        return self.dir.y != 0

    def _is_moving_horiz(self):
        """True if the marble is moving horizontally."""
        return self.dir.x != 0

    def _change_dir_with_func(self, new_dir_lambda):
        self.dir = new_dir_lambda(self.dir)

    def _calculate_direction(self):
        """Calculate the inial direction of a just created marble."""
        valid_chars = r'\/*^v><+═║╔╗╚╝'

        for direction in DIRECTIONS:
            loc = self.pos + direction

            # we have no interest in chars outside
            if not self.env.world.does_loc_exist(loc):
                continue

            if direction in (UP, DOWN) and self.env.world.get_char_at(loc) == '|':
                return direction

            if direction in (LEFT, RIGHT) and self.env.world.get_char_at(loc) == '-':
                return direction

            if self.env.world.get_char_at(loc) in valid_chars:
                return direction

        # If we get here without returning, the marble can't find a direction to go!
        self.env.io.on_error("marble cannot determine location...\nx: {}, y: {}".format(*self.pos))

        self.is_dead = True
        return Pos(0, 0)
