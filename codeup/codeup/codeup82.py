"""
82번. 친구들과 함께 3 6 9 게임을 하던 영일이는 잦은 실수 때문에 계속해서 벌칙을 받게 되었다.
3 6 9 게임의 왕이 되기 위한 369 마스터 프로그램을 작성해 보자.
"""
num = int(input())

for i in range(1, num + 1):

    if "3" in str(i) or "6" in str(i) or "9" in str(i):
        print("X", end=" ")
    else:
        print(i, end=" ")