import lark

from . import api


class NukeScriptTransformer(lark.Transformer):

    CNAME = str
    ESCAPED_STRING = str
    LITERAL = str
    SIGNED_NUMBER = float
    STRING = str

    def start(self, args):
        return args

    def node(self, args):
        return api.Node(next(x for x in args if not isinstance(x, api.Knob)), {x.name(): x for x in args if isinstance(x, api.Knob)})

    def ntype(self, args):
        return args[0]

    def knob(self, args):
        return api.Knob(*args)

    def name(self, args):
        return args[0]

    def value(self, args):
        return args[0]

    def curve(self, args):
        return api.AnimationCurve(args)

    def key(self, args):
        return api.AnimationKey(*args)

    def x(self, args):
        return args[0]

    def y(self, args):
        return args[0]
