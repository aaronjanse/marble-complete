import threading

from .marble import Marble
from .world import World


class AsciiMarblesInterpreter(object):
    def __init__(self, env, program, program_dir):
        """
        Create a new instance of the interpreter to run the program.

        :param marbles.environement.Env env: The environement for the program
        :param str program: The code of the program
        :param str program_dir: The path to the program directory
        """

        self.env = env
        self.env.interpreter = self
        self.env.world = World(env, program, program_dir)
        self.env.marbles = []

        self.needs_shutdown = False

        self._setup_marbles()

    def _setup_marbles(self):
        """Fill the marble list with marbles from the starting points in the world."""

        self.env.marbles = []
        for pos in self.env.world.get_coords_of_marbles():
            new_marble = Marble(self.env, pos)

            self.env.marbles.append(new_marble)

    def run(self, run_in_separate_thread=None, make_thread_daemon=None):
        """
        Start executing the AsciiMarbles code

        Arguments:
        run_in_separate_thread -- If set to True, the program will be interpreted in a separate thread
        make_thread_daemon -- Controls whether a thread created by enabling in_seperate_thread will be run as daemon
        """

        if run_in_separate_thread:
            inter_thread = threading.Thread(
                target=self.run, daemon=make_thread_daemon)
            inter_thread.start()
            return

        while not self.needs_shutdown and len(self.env.marbles) > 0:
            next_tick_marbles = []

            for marble in self.env.marbles:
                marble.simulate_tick()

                if not marble.is_dead:
                    next_tick_marbles += marble,

            self.env.io.on_microtick(self.env.marbles[0])

            self.env.marbles = next_tick_marbles

        self.env.io.on_finish()

    def terminate(self):
        """The program will shut down at the next operation."""
        self.needs_shutdown = True
