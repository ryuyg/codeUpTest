"""
97번. 부모님과 함께 놀러간 영일이는
설탕과자(설탕을 녹여 물고기 등의 모양을 만든 것) 뽑기를 보게 되었다.

길이가 다른 몇 개의 막대를 바둑판과 같은 격자판에 놓는데,

막대에 있는 설탕과자 이름 아래에 있는 번호를 뽑으면 설탕과자를 가져가는 게임이었다.
(잉어, 붕어, 용 등 여러 가지가 적혀있다.)

격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
막대를 놓는 방향(d:가로는 0, 세로는 1)과
막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,

격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.
"""
#판 만들기.
borad = []

boradSizeX, boradSizeY = input().split()
boradSizeX, boradSizeY = int(boradSizeX),int(boradSizeY)

for i in range(boradSizeX):
    borad.append([])
    for j in range(boradSizeY):
        borad[i].append(0)
#판에 막대 넣기 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l)
#막대의 길이 (ragne->r , 방향 dir ->d 0 가로 Y 1 세로 X, 좌표 YX 순 -> x y )
#input 4개 -> x y d r
#입력값 총 2개

#막대 갯수
stcikCount = int(input())
#print("길이, 방향(0->가로, 1->세로), x y -> 시작 좌표(인덱스)")
for i in range(stcikCount):
    r, d, x, y  = map(int, input().split())

    #x, y 에서 가로축으로 길이만큼 r   
    if d == 0:
        for i in range(boradSizeY):
            for i in range(r):
                borad[x-1][y+i-1] = 1 
    #x, y 에서 세로축으로 X 길이만큼 r
    else:
        for i in range(boradSizeX):
            for i in range(r):
                borad[x+i-1][y-1] = 1 


#최종 출력
for i in range(boradSizeX):
    for j in range(boradSizeY):
        print(borad[i][j], end=' ')
    print()
