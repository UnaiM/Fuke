class AnimationKey(object):

    def __init__(self, x, y):
        super(AnimationKey, self).__init__()
        self.x = x
        self.y = y


class AnimationCurve(object):

    EPSILON = 0.0001

    def __init__(self, keys):
        super(AnimationCurve, self).__init__()
        self.__keys = keys

    def evaluate(self, t):
        dist = {}
        for key in self.__keys:
            d = abs(key.x - t)
            if d <= self.EPSILON:
                dist[d] = key.y
        if not dist:
            raise NotImplementedError('Only keyframe values are retrievable.')
        return dist[min(dist)]

    def keys(self):
        return self.__keys


class Knob(object):

    def __init__(self, name, value):
        super(Knob, self).__init__()
        self.__name = name
        self.__value = value

    def animation(self):
        if self.isAnimated():
            return self.__value

    def isAnimated(self):
        return isinstance(self.__value, AnimationCurve)

    def name(self):
        return self.__name

    def getValue(self):
        if self.isAnimated():
            return self.valueAt(0)
        return self.__value

    def getValueAt(self, t):
        if self.isAnimated():
            return self.__value.evaluate(t)
        return self.__value

    value = getValue
    valueAt = getValueAt


class Node(object):

    def __init__(self, class_, knobs):
        super(Node, self).__init__()
        self.__class = class_
        self.__knobs = knobs

    def __getitem__(self, y):
        return self.__knobs[y]

    def Class(self):
        return self.__class

    def allKnobs(self):
        return list(self.__knobs.values())

    def knob(self, p):
        return self.__knobs[p]

    def knobs(self):
        return self.__knobs
