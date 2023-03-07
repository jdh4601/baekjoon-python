import sys
sys.stdin = open("input.txt", "r")
lst = list(map(int, input().split()))

num1 = int(str(lst[0]) + str(lst[1]))
num2 = int(str(lst[2]) + str(lst[3]))

print(num1 + num2)