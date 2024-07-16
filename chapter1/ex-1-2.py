"""
1.2.1 수치형 흉내 내기

연산자 (ex: +) 에 사용자 정의 객체가 응답할 수 있게 특별 메서드 구현
"""

import doctest
from math import hypot

"""
>>> Vector(1, 2)  # ( __repr__() )
Vector(1, 2)

>>> v1 = Vector(2, 4)  # x, y 좌표
>>> v2 = Vector(2, 1)
>>> v1 + v2  # 벡터 덧셈  ( __add__() )
Vector(4, 5)

>>> v = Vector(3, 4)
>>> abs(v)  # 벡터의 크기  ( __abs__() )
5.0

>>> v * 3  # 벡터의 스칼라곱 ( __mul__() )
Vector(9, 12)
>>> abs(v * 3)
15.0
"""


class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        """
        >>> Vector(1, 2)
        Vector(1, 2)
        >>> Vector('1', '2')
        Vector('1', '2')
        """
        return "Vector(%r, %r)" % (self.x, self.y)

    def __abs__(self):
        """
        >>> abs(Vector(3, 4))
        5.0
        >>> abs(Vector(0, 0))
        0.0
        >>> abs(Vector(3, -4))
        5.0
        >>> abs(Vector(-3, -4))
        5.0
        """
        return hypot(self.x, self.y)

    def __bool__(self):
        """
        >>> bool(Vector(3, 4))
        True
        >>> bool(Vector(0, 0))
        False
        >>> bool(Vector(3, -4))
        True
        >>> bool(Vector(-3, -4))
        True
        """
        return bool(abs(self))

    def __add__(self, other: "Vector"):
        """
        >>> Vector(2, 4) + Vector(2, 1)
        Vector(4, 5)
        >>> Vector(1, 1) + Vector(-1, -2)
        Vector(0, -1)
        """
        x = self.x + other.x
        y = self.y + other.y
        # 중위연산자는 의례적으로 피연산자를 변경하지 않고 새로운 객체를 생성하여 반환
        return Vector(x, y)

    def __mul__(self, scalar: int):
        """
        >>> Vector(1, 1) * 3
        Vector(3, 3)
        >>> Vector(1, 1) * -3
        Vector(-3, -3)
        >>> Vector(1, 1) * 0
        Vector(0, 0)
        """
        # 중위연산자는 의례적으로 피연산자를 변경하지 않고 새로운 객체를 생성하여 반환
        return Vector(self.x * scalar, self.y * scalar)


doctest.testmod(verbose=True)
