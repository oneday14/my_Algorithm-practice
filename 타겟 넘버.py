# URL : https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    answer = 0
    for i in range(0, len(numbers)) :
        answer += 1
        numbers[i] = (-1) * numbers[i] 
        if sum(numbers) == target :
            break
        
    a = 1
    b = 1
    for i in range(1, answer + 1) :
        a = a * ((len(numbers) + 1) - i)
        b = b * i
    
    return a/b

solution([1,1,1,1,1], 3)
