def solution(num_list):
    check = 1
    check2 = 0

    for i in num_list:
        #모든 원소 곱
        check *= i
        #모든 원소 합의 제곱
        check2 += i     
        
    if check < check2**2:
        return 1
    else:
        return 0