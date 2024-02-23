"""
Decorators for GenTopo methods
"""

import functools


class Registry(object):
    def __init__(self):
        # TODO: Include reference to version of package?
        pass

    def register(self, method):
        name = getattr(method, "__name__", str(method))
        setattr(self, name, method)
