# 체육복

def solution(n, lost, reserve):
    answer = n
    for i in reserve:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
            
    for i in range(len(lost)):
        answer -= 1
        if lost[i] in reserve:
            answer += 1
            reserve.remove(lost[i])
        elif lost[i]-1 in reserve:
            answer += 1
            reserve.remove(lost[i]-1)
        elif lost[i]+1 in reserve:
            answer += 1
            reserve.remove(lost[i]+1)

    return answer