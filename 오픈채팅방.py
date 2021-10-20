# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    d1 = {}
    answer = []
    for i in record :
        split_str = i.split(' ')
        if len(split_str) == 3 :
            d1[split_str[1]] = split_str[2]
            
    for i in record :
        split_str = i.split(' ')        
        if split_str[0] in ('Enter') :   
            action = "들어왔습니다."
            answer.append(d1.get(split_str[1]) + '님이 ' + action)
        elif split_str[0] == 'Leave' :
            action = "나갔습니다."
            answer.append(d1.get(split_str[1]) + '님이 ' + action)
        else :
            pass
          
    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
