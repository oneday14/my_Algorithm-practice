# url : https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    string = ''
    lst_num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    lst_seq = [i for i in range(0, 10)]
    answer = ''
    
    for i in s :
        if i.isalpha() :
            string += i
            if string in lst_num :
                answer += str(lst_seq[lst_num.index(string)])
                string = ''
            else : 
                pass
        else : 
            answer += str(i)
    
    return answer

solution('one4seveneight')
solution('23four5six7')
solution('2three45sixseven')
solution('123')
