def solution(num_list):
    answer = []
    for i in range(0,len(num_list)):
        answer.append(num_list[i])
        if i == len(num_list)-1:
            print(num_list[i])
            if num_list[i] <= num_list[i-1]:
                answer.append(num_list[i] * 2)
            else:
                answer.append(num_list[i] - (num_list[i - 1]))               
                
    return answer