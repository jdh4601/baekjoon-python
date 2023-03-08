import sys
sys.stdin = open("input.txt", "r")

# 에라토스테네스의 체
array = [True for i in range(1000001)]

for i in range(2, 1001):
    if array[i]:
        for k in range(i + i, 1000001, i):
            array[k] = False

while True:
    try:
        n = int(sys.stdin.readline())
        
        if n == 0:
            break
        
        for i in range(3, len(array)):
            if array[i] and array[i - 1]:
                print(f'{n} = {i} + {n-i}')
                break
    except:
        break