import os

import lark

from .api import *
from . import transformer


class Fuke(object):

    def __init__(self):
        super(Fuke, self).__init__()
        self.__nodes = []

    def allNodes(self, filter=None):
        if filter:
            return [x for x in self.__nodes if x.Class() == filter]
        return self.__nodes

    def scriptOpen(self, nkfile):
        with open(os.path.join(os.path.dirname(__file__), 'nuke_script.lark')) as f:
            parser = lark.Lark(f)
        with open(nkfile) as f:
            tree = parser.parse(f.read())
        self.__nodes = transformer.NukeScriptTransformer().transform(tree)
