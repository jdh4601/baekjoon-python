import sys
sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
# [3 5 2 7]
arr = list(map(int, sys.stdin.readline().split()))
stk = [] # 인덱스 할당
answer = [-1] * n # [-1 -1 -1 -1]
for i in range(n):
    # stk이 비어있지 않고 '현재 원소'가 '오른쪽 원소들'보다 크면?
    while stk and arr[stk[-1]] < arr[i]:
        answer[stk.pop()] = arr[i]
    # 맨앞 원소가 현재 원소보다 작으면?
    stk.append(i)  # stk에 인덱스를 추가 +0
    
print(*answer)