class Env(object):
    """
    A container for all the importants parts of an Asciimarbles program.
    """

    def __init__(self, world=None, marbles=None, io=None, interpreter=None):
        """
        Structure for the for important parts of a marbles environement.

        If you don't pass one of the 4 parameters, you need to set them quickly.

        :type world: marbles.world.World
        :type marbles: list[marbles.marble.Marble]
        :type io: marbles.callbacks.IOCallbacksStorage
        :type interpreter: marbles.interpreter.AsciiMarblesInterpreter
        """

        self.world = world
        self.marbles = marbles
        self.io = io
        self.interpreter = interpreter



