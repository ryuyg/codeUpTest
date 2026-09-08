def solution(number, n, m):
    
    #공배수이면. 즉 n 과 m 둘 다 나머지계싼시 0 이 나오는 숫자가 1
    return (1 if ((number % n == 0 )& (number % m == 0)) else  0)