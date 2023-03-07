import sys
sys.stdin = open("input.txt", "r")
str = sys.stdin.readline()

arr = []

for i in range(len(str)):
    new = str[i:]    
    arr.append(new)

for j in sorted(arr):
    print(j)