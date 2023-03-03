import sys
sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline()) # 15

queue = []

for _ in range(n):
    x = sys.stdin.readline().split()
    
    if x[0] == 'push':
        queue.insert(0, x[1])
    if x[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    if x[0] == 'size':
        print(len(queue))
    if x[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    if x[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    if x[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])