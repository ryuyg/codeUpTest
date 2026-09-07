def solution(str1, str2):
    new_string = []
    for i in range(len(str1)):
        new_string.append(str1[i])
        new_string.append(str2[i])
    answer = ''.join(new_string)
    return answer
