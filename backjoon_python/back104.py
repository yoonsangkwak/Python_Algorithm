# 11729번
# https://yoonsang-it.tistory.com/

n = int(input())

def move_disk(disk_num, start_peg, end_peg):
    print(f"{start_peg} {end_peg}")

def hanoi(num_disks, start_peg, end_peg):
    if num_disks == 1:
        return move_disk(num_disks, start_peg, end_peg)
    
    other_peg = 6 - start_peg - end_peg
    hanoi(num_disks-1, start_peg, other_peg)
    move_disk(num_disks, start_peg, end_peg)
    hanoi(num_disks-1, other_peg, end_peg)

def count(n):
    if n == 1:
        return 1
    
    return count(n - 1) + 2 ** (n - 1)

print(count(n))
hanoi(n, 1, 3)