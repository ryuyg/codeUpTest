"""
63번. 입력된 두 정수(a, b) 중 큰 값을 출력하는 프로그램을 작성해보자.
단, 3항 연산을 사용한다.
"""

a, b = input().split()
a, b = int(a), int(b)

c = (a if a>b else b)
print(c)