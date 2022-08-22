__version__ = '0.1.0'


class A:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def minus(self):
        return self.a - self.b


class B(A):
    def sum(self):
        return self.a + self.b


value = A(1, 2)
value2 = B(3, 4)

print(value.minus())
print(value2.sum())
