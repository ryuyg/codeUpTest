"""
98번. 영일이는 생명과학에 관심이 생겨 왕개미를 연구하고 있었다.

왕개미를 유심히 살펴보던 중 특별히 성실해 보이는 개미가 있었는데,
그 개미는 개미굴에서 나와 먹이까지 가장 빠른 길로 이동하는 것이었다.

개미는 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직여 가장 빠른 길로 움직였다.
(오른쪽에 길이 나타나면 다시 오른쪽으로 움직인다.)

이에 호기심이 생긴 영일이는 그 개미를 미로 상자에 넣고 살펴보기 시작하였다.

미로 상자에 넣은 개미는 먹이를 찾았거나, 더 이상 움직일 수 없을 때까지
오른쪽 또는 아래쪽으로만 움직였다.

미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.

단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는
더이상 이동하지 않고 그 곳에 머무른다고 가정한다.

미로 상자의 테두리는 모두 벽으로 되어 있으며,
개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발한다.
"""
#---------------------------------------------------------------------------------------
#초기 맵 생성
board = []
boardSizeX, boardSizeY = map(int, input().split())
for i in range(boardSizeX):
    board.append([])
    for j in range(boardSizeY):
        board[i].append(0)

# if d == 0:
#             for i in range(r):
#                 borad[x-1][y+i-1] = 1 
#----------------------------------------------------------------------------------------
#맵 셋팅 - code 업 입력예시 기준
# 1 1 1 1 1 1 1 1 1 1
# 1 0 0 1 0 0 0 0 0 1
# 1 0 0 1 1 1 0 0 0 1
# 1 0 0 0 0 0 0 1 0 1
# 1 0 0 0 0 0 0 1 0 1
# 1 0 0 0 0 1 0 1 0 1
# 1 0 0 0 0 1 2 1 0 1
# 1 0 0 0 0 1 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 1 1 1 1 1 1 1 1 1
# def setWall(wall):
#     newWall = wall.copy()
#     for i in range(len(wall)):
#         newWall[i] = 1
#     
#     return wall

#외벽
for i in range(boardSizeX):   
    for j in range(boardSizeY):
        #x축 j , #y축 i 
        #처음 벽. 끝 벽
        if i == 0 or j == 0 or i == (boardSizeX-1) or j == (boardSizeY-1):
            board[i][j] = 1
#내벽
board[1][3] =1
board[2][3] =1
board[2][4] =1
board[2][5] =1
board[5][5] =1
board[6][5] =1
board[7][5] =1
board[3][7] =1
board[4][7] =1
board[5][7] =1
board[6][7] =1

#개미와 먹이 위치 세팅.개미 2x2 
#나중엔 input으로도 가능하게 해보기
#개미 위치
antPointX = 1
antPointY = 1
board[antPointX][antPointY]
#먹이위치
foodPointX = 6
foodPointY = 6
board[foodPointX][foodPointY] = 2

# wallList = [, , ]
# setWall(wallList)
#-----------------------------------------------------------------------------------------
#먹이찾기 알고리즘
#시작지점 (개미) -> 도착지점 (먹이)
#먹이 좌표 - 개미 좌표 해서 남는 x y 만큼 이동.
#다만, 벽에 부딪히면 다시 이동 좌표 설정
moveCountX = foodPointX - antPointX
moveCountY = foodPointY - antPointY 
isFindFood = False

#음식을 찾기 전까지는 반복돌리며 경로 찾기.
while(isFindFood == 0):
    if moveCountX != 0 & moveCountX != 0:
        if board[antPointX + 1][antPointY] != 1: 
            antPointX += 1
            moveCountX -= 1
            board[antPointX][antPointY] = 9
        else:
            antPointY += 1
            moveCountX -= 1
            board[antPointX][antPointY] = 9

    #종료 조건.
    if antPointX == foodPointX & antPointY == foodPointY:
        board[antPointX][antPointY] = 9
        isFindFood =True





#최종 출력---------------------------------------------------------------------------------
for i in range(boardSizeX):
    for j in range(boardSizeY):
        print(board[i][j], end=' ')
    print()
