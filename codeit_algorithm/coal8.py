def move_disk(disk_num, start_peg, end_peg):
    print(f"{disk_num}번 원판을 {start_peg}번 기둥에서 {end_peg}번 기둥으로 이동")

def hanoi(num_disks, start_peg, end_peg):
    # 코드를 입력하세요.
    if num_disks == 1:
        return move_disk(num_disks, start_peg, end_peg)
    
    other_peg = 6 - start_peg - end_peg
    hanoi(num_disks-1, start_peg, other_peg)
    move_disk(num_disks, start_peg, end_peg)
    hanoi(num_disks-1, other_peg, end_peg)

# 테스트 코드 (포함하여 제출해주세요)
hanoi(3, 1, 3)