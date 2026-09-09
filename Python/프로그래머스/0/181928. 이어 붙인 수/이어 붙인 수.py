
def solution(num_list):
    sum_num1 = []
    sum_num2 = []
    for i in num_list:
        if i % 2 == 0:
            sum_num1 += str(i)
        else:
            sum_num2 += str(i).split()

    answer = int(''.join(sum_num1)) + int(''.join(sum_num2))
    
    return answer