"""
93번. 정보 선생님은 수업을 시작하기 전에 이상한 출석을 부른다.

학생들의 얼굴과 이름을 빨리 익히기 위해 번호를 무작위(랜덤)으로 부르는데,
영일이는 선생님이 부른 번호들을 기억하고 있다가 거꾸로 불러보는 것을 해보고 싶어졌다.

출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력해 보자.
"""

callCount = int(input())
callnum = input().split()
studentNum = []

for i in range(0,callCount):
    callnum[i] = int(callnum[i])

for i in range(0,callCount):
    studentNum.append(0)

for i in range(0,callCount):
    studentNum[i] = callnum[i]

studentNum = studentNum[::-1]

for i in range(0, callCount) :  #카운트한 값을 공백을 두고 출력
    print(studentNum[i], end=' ')
