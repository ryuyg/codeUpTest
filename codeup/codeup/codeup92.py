"""
92번. 정보 선생님은 수업을 시작하기 전에 이상한 출석을 부른다.

선생님은 출석부를 보고 번호를 부르는데,
학생들의 얼굴과 이름을 빨리 익히기 위해 번호를 무작위(랜덤)으로 부른다.

그리고 얼굴과 이름이 잘 기억되지 않는 학생들은 번호를 여러 번 불러
이름과 얼굴을 빨리 익히려고 하는 것이다.

출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.
"""

totalstudent = 23
callcount = int(input())
callednum = input().split()

calledstudent =[]
for i in range(0,len(callednum)):
    callednum[i] = int(callednum[i])

for i in range(0,totalstudent+1):
    calledstudent.append(0)

for i in range(0,callcount):
    calledstudent[callednum[i]] +=1

# for i in range(0,callcount):
#     a = int(input())
#     callednum[a] += 1

for i in range(1, totalstudent+1) :  #카운트한 값을 공백을 두고 출력
    print(calledstudent[i], end=' ')