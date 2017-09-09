class Char(str):
    def __init__(self, value):
        self.value = value

    def isMarble(self):
        return False

    def isOper(self):
        return False

    def isCurlyOper(self):
        return False

    def isSquareOper(self):
        return False


class MarbleChar(Char):
    def isMarble(self):
        return True


class OperChar(Char):
    def __init__(self, value):
        super().__init__(value)

        self.func = None

    def isOper(self):
        return True

    def calc(self, x, y):
        if self.func is None:
            function_dict = {
                '+': (lambda x, y: x + y),
                '-': (lambda x, y: x - y),
                '*': (lambda x, y: x * y),
                '/': (lambda x, y: x / y),
                '÷': (lambda x, y: x / y),
                '^': (lambda x, y: x ** y),
                '%': (lambda x, y: x % y),

                'o': (lambda x, y: x | y),
                'x': (lambda x, y: x ^ y),
                '&': (lambda x, y: x & y),
                '!': (lambda x, y: x != y),

                '=': (lambda x, y: x == y),
                '≠': (lambda x, y: x != y),
                '>': (lambda x, y: x > y),
                '≥': (lambda x, y: x >= y),
                '<': (lambda x, y: x < y),
                '≤': (lambda x, y: x <= y)
            }

            self.func = function_dict[self]

        return self.func(x, y)


class CurlyOperChar(OperChar):
    def isCurlyOper(self):
        return True


class SquareOperChar(OperChar):
    def isSquareOper(self):
        return True
