import sys
sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    A, B = a, b
    while a != 0:
        b = b % a
        b, a = a, b
    print(A * B // b)
