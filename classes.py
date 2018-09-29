class MyFirstClass:
    param2 = 'param2'

    def method1(self, arg1, arg2):
        print(arg1, arg2)

    @staticmethod
    def static_method(arg1, arg2):
        print(arg1, arg2)

    @classmethod
    def class_method(cls, arg1, arg2):
        cls.static_method(arg1, arg2)


my_class = MyFirstClass()
my_class.param1 = 'param1'
print(my_class.param1)
print(my_class.param2)


my_class.method1('1', '2')
MyFirstClass.static_method('s1', 's2')
my_class.static_method('s1', 's2')

print('///////'*10)


class MyFirstClass2:
    def foo1(self):
        print(self)

    @classmethod
    def foo2(cls):
        print(cls)

class2 = MyFirstClass2()
class2.foo1()
class2.foo2()


class ClassParams:
    public = 1
    CONST = 1
    _private = 1

    def public_method(self):
        pass

    def _private_method(self):
        pass

c = ClassParams()


class Animal:
    def voice(self):
        print('')


class Dog(Animal):
    def voice(self):
        print('Wow!')


class Cat(Animal):
    def voice(self):
        print('Meow!')


a = Animal()
c = Cat()
d = Dog()

print('/////'*10)
a.voice(), c.voice(), d.voice()

# for python2
class Old:
    pass


class New(object):
    pass


# class with params

class ClassWithParams:

    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

c = ClassWithParams('1', '2')
print(c.arg1, c.arg2)


print('MAGIC METHODS')

class ClassWithMagicMethods:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __le__(self, other):
        return self.value <= other.value

    def __abs__(self):
        return abs(self.value)

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other

    def __rsub__(self, other):
        return other - self.value

    def __mod__(self, other):
        pass

    def __iadd__(self, other):
        self.value += other
        return self

    def __str__(self):
        return "STR" + str(self.value)


c1 = ClassWithMagicMethods(123)
c2 = ClassWithMagicMethods(123)

print(c1 == c2)
print(abs(c1))
print(c1 + c2)
print(c1 - 3)
print(3 - c1)

c1 += 3

print(c1.value)
print(str(c1))