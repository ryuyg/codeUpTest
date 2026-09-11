

#         for i in range(1,n+1,2):
#             answer += i
#     else:
#         for i in range(2,n+1,2):
#             answer += i**2
#     return answer
###----------------------------------------------------


#-------------------공배수 삼항연산자로 풀기--------------------------------
# def solution(number, n, m):
#     #공배수이면. 즉 n 과 m 둘 다 나머지계싼시 0 이 나오는 숫자가 1
#     return (1 if (number % n == 0 & number % m == 0) else  0)
#-----------------------------------------------------------------------

# def solution(a, b, flag): 
#     return (a + b) if flag == 1 else (a - b)

#------------------------------------------------------------------------
# def solution(a, b, c):                                                                                                                                                                                                                                                          
#     answer=0
#     if (a != b) & (a!=c) & (c!=b):
#         answer = a+b+c
#     elif (a==b) & (b==c) & (c==a):
#         answer = (a+b+c)*(a**2 + b**2 + c**2)*(a**3+b**3+c**3)
#     else:
#         answer = (a+b+c)*(a**2 + b**2 + c**2)

#     return answer
####------------------->1줄로 줄여보기-------------------------------------
# def solution(a, b, c):
#     return (a+b+c)*(a**2 + b**2 + c**2)*(a**3+b**3+c**3) if (a==b) & (b==c) & (c==a) else (a+b+c if (a != b) & (a!=c) & (c!=b) else (a+b+c)*(a**2 + b**2 + c**2))
##-----------------------------------------------------------------------
"""
정수가 담긴 리스트 num_list가 주어집니다. 
num_list의 홀수만 순서대로 이어 붙인 수 str으로 합치고 int 로 반환
와 짝수만 순서대로 이어 붙인 수의 합을 str으로 합치고 int 로 반환
return하도록 solution 함수를 완성해주세요.
"""
# number = [3, 4, 5, 2, 1]
# number2 = [5, 7, 8, 3]

# def solution(num_list):
#     sum_num1 = []
#     sum_num2 = []
#     for i in num_list:
#         if i % 2 == 0:
#             sum_num1 += str(i)
#         else:
#             sum_num2 += str(i).split()

#     answer = int(''.join(sum_num1)) + int(''.join(sum_num2))
    
#     return answer

# print(solution(number2))

"""
정수 리스트 num_list가 주어질 때, 
num_list > num_list - 1 -> append(num_list - (num_list - 1))
num_list < num_list - 1 -> append(num_list*2)
마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을 
마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가하여
return하도록 solution 함수를 완성해주세요.
"""
# num_list = [5, 2, 1, 7, 5]
# num_list2 = [2, 1, 6]

# def solution(num_list):

#     answer = []
#     for i in range(0,len(num_list)):
#         answer.append(num_list[i])
#         if i == len(num_list)-1:
#             print(num_list[i])
#             if num_list[i] <= num_list[i-1]:
#                 answer.append(num_list[i] * 2)
#             else:
#                 answer.append(num_list[i] - (num_list[i - 1]))               
                
#     return answer

# print(solution(num_list2))

"""
정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 모든 
정수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다
 """
# a = 5
# b = 555
# def solution(l, r):

#     answer = []
#     for i in range(l,r):
#         if 

# print(solution(a , b))
# num = 10
# def solution(n): 
#     answer = []
#     while (n>1):
#         answer.append(n)
#         if n % 2 ==0:
#             n //= 2             
#         else:
#             n = (3*n + 1)
#     answer.append(n)
#     return answer
# print(solution(num))

"""
만약 stk가 빈 배열이라면 arr[i]를 stk에 추가하고 i에 1을 더합니다.
stk에 원소가 있고, stk의 마지막 원소가 arr[i]보다 작으면 arr[i]를 stk의 뒤에 추가하고 i에 1을 더합니다.
stk에 원소가 있는데 stk의 마지막 원소가 arr[i]보다 크거나 같으면 stk의 마지막 원소를 stk에서 제거합니
"""
numbers = [1, 4, 2, 5, 3]

def solution(arr):
    stk = []
    i = 0 
    while (i < len(arr)):
        if len(stk) == 0 :
            stk.append(arr[i])
            print(stk)
            i += 1
        else:
            if stk[len(stk-1)] < arr[i]:
                stk.append(arr[i])
                i += 1
            else: #stk[len(stk-1)] >= arr[i]
                stk.pop(stk[len(stk-1)])
            
            print(stk)

    return stk
    
print(solution(numbers))