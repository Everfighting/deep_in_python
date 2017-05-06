# coding:utf-8

class Foo(object):
    X = 1
    Y = 2

    @staticmethod
    def average(*mixes):
        return sum(mixes)/len(mixes)

    @staticmethod
    def static_method():
        return Foo.average(Foo.X, Foo.Y)

    @classmethod
    def class_method(cls):
        return cls.average(cls.X, cls.Y)

class Son(Foo):
    X = 3
    Y = 5

    @staticmethod
    def average(*mixes):
        return sum(mixes)/3

p = Son()
print(p.static_method())
print(p.class_method())