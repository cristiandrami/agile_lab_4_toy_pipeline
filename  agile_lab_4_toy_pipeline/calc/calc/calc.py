import functools


class Calc:

    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def mul(self, *args):
        if any(type(arg) is not int for arg in args):
            raise TypeError

        res = functools.reduce(lambda a, b: a * b, args, 1)

        if res == 0:
            raise ValueError

        return res

    def div(self, a, b):
        return a / b if b != 0 else 'inf'

    def avg(self, it, ut=None, lt=None):
        if lt is not None:
            it = [x for x in it if x >= lt]

        if ut is not None:
            it = [x for x in it if x <= ut]

        if not it:
            return None

        return sum(it) / len(it)

