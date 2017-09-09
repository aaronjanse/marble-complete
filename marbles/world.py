# Char inheritance works similar to the Decorator Pattern

# TODO: make the iters have a default arg of self._data_array?

import os

from marbles.vector import Pos
from .chars import *


class World(object):
    def __init__(self, env, world_map, program_dir):
        """
        Create a new world to do marbles races !

        :param marbles.environement.Env env: The environement for the program
        :param str world_map: The string representing the world.
        :param str program_dir: The directory of the program
        """

        self.env = env
        self.env.world = self

        self.program_dir = program_dir

        self.map = self.map_from_raw(world_map)

        self._setup_operators()

        self._update_class_of_marbles()

    def get_coords_of_marbles(self):
        """Yiels the cordinates of every marble char in the world."""
        for y, line in enumerate(self.map):
            if line[0] == '%':
                continue

            for x, char in enumerate(line):
                if char.isMarble():
                    yield Pos(x, y)

    # ✓
    def get_char_at(self, pos: Pos):
        """Get the Char at the given position."""
        # NOTE: _data_array has to be accesed using y, x due to the way it is created
        return self.map[pos.row][pos.col]

    # ✓
    def does_loc_exist(self, loc: Pos):
        """True if this location exists on the map."""
        return 0 <= loc.row < len(self.map) and 0 <= loc.col < len(self.map[loc.row])

    # TODO check if the char is inside of a ascii marbles text string
    def _update_class_of_marbles(self):
        for y, char_list in enumerate(self.map):
            last_was_backtick = False
            for x, char in enumerate(char_list):
                if char == '`':
                    if not last_was_backtick:
                        last_was_backtick = True
                    else:
                        break

                if char == 'o':
                    self.map[y][x] = MarbleChar(char)

    # ✓
    def _setup_operators(self):
        for y, line in enumerate(self.map):
            for x, char in enumerate(line):
                if char in 't↘T↙':
                    self.map[y][x] = Toggler(char)

    # ✓
    def _char_obj_array_iter(self, obj_array):
        for char_list in obj_array:
            for char in char_list:
                yield char

    # ✓
    def _char_obj_array_iter_with_coords(self, obj_array):
        for y, char_list in enumerate(obj_array):
            for x, char in enumerate(char_list):
                yield Pos(x, y), char

    # ✓✓
    @staticmethod
    def map_from_raw(raw_map: str):
        """
        Convert a code in a string to a usable map.

        This will suppress the comments and convert each chr of the string to the corresponding Char.
        Creates a 2D array accessible by map[row][col].
        :param str raw_map: The program as it is stored in files.
        """

        map = []

        # for each line
        for raw_line in raw_map.split('\n'):
            # removing the comments
            line = raw_line.partition('``')[0] + ' '
            # Convert the str to a list of Char
            line = [Char(c) for c in line]
            # add aech row to the map
            map.append(line)

        return map
