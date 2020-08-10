def consecutive_sum(start, end):
    # 코드를 작성하세요
    center = (start + end) // 2
    def left_sum(start, center):
        if center == start:
            return start
        return center + left_sum(start, center - 1)
    
    def right_sum(center, end):
        if end == center + 1:
            return center + 1
        return end + right_sum(center, end - 1)
    
    return left_sum(start, center) + right_sum(center, end)

# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))