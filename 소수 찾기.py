# https://programmers.co.kr/learn/courses/30/lessons/42839

# 문제 설명
# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 
# 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 
# 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# - numbers는 길이 1 이상 7 이하인 문자열입니다.
# - numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# - '013'은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

def solution(numbers):
    import itertools
    
    num = [int(i) for i in numbers]
    events = []
    for i in range(1, len(num) + 1) :
        events.append(list(itertools.permutations(num, i)))
        
    string = ''
    lst = []
    for i in events :
        for j in i :
            for k in j :
                string += str(k)
            lst.append(int(string))
            string = ''
          
    lst = list(set(lst))
    common = []
    answer = 0
    for i in lst :
        if i != 0 and i != 1 :
            for j in range(1, i//2 + 1) :
                if i % j == 0 :
                    common.append(j)
            if len(common) == 1 :
                answer += 1
            common = []
            
    return answer

solution('17')
solution('011')
