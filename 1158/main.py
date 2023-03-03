import sys
sys.stdin = open("input.txt", "r")
n, k = map(int, sys.stdin.readline().split())

arr = [i for i in range(1, n + 1)]
num = 0  # 제거되는 수의 인덱스
answer = []  # 제거되는 수 순서대로

for _ in range(n):
    num += k-1  # +2 더함
    if num >= len(arr):  # 한바퀴 돈다면? -> num 앞으로
        num = num % len(arr)
    val = arr.pop(num)
    answer.append(str(val))

print(f"<{', '.join(answer)}>")