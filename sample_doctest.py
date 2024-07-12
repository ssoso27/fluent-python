"""
doctest 를 사용한 간단한 테스트 코드

1. import doctest
2. 함수 정의
3. 함수에 대한 테스트 코드를 docstring 으로 작성
4. doctest.testmod() 함수를 호출하여 테스트 실행
5. python sample_doctest.py -v
"""

import doctest


def add(num1: int, num2: int) -> int:
    """
    num1 과 num2 를 더한 값을 리턴한다.

    >>> add(1, 2)
    3
    >>> add(10, -1)
    9
    """
    return num1 + num2


doctest.testmod()
