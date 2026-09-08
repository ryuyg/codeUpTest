def solution(n):  
    total_odd = 0
    total_even = 0
    for i in range(n+1):
        if i % 2 == 0:
            total_even += (i**2)
        else:
            total_odd += i
    # for i in range(0,n):
    #     #짝수
    #     if i % 2 == 0:
    #         answer = (i*i)
    #         total += answer
    #     #홀수
    #     else:
    #         total += i
         
    # answer = total
    if n % 2 == 0:
        return total_even
    else:
        return total_odd