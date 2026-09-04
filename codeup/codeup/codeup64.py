"""
64번. 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
단, 3항 연산을 사용한다.
"""

a,b,c = input().split()
a,b,c = int(a),int(b),int(c)
lowNum = 0
if a > b :
    if b > c: 
        print(c)
    else:
        print(b)
elif b > c:
    if a > c: 
        print(c)
    else:
        print(a)
else: 
    if a > b:
        print(b)
    else:
        print(a)