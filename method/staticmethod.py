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

foo = Foo()
print(foo.static_method()) #实例的静态方法
print(foo.class_method()) # 实例的类方法